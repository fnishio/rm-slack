import broadlink
from datetime import datetime

# IR codes
ceiling_light = {
    'on' : '260058000001279512131238121411141213121312141139123812141139113912131239113912131238123912381238123912381214113911141213121312141114121312381214110005530001274b12000c720001274b12000d05',
    'fav' : '2600580000012a9215111436141114121411141114111436153614111436153614111436143714111411143615111411141114371411143614361511143614361437141114361412140005510001294914000c700001294914000d05',
    'bright' : '260058000001299314121436141114121312141114111436143714111436143713121436143713121312133714121337143614371312133714371312133714111412131214361411140005510001284b12000c7100012a4914000d05',
    'dark' : '260050000001299314111436141214111411141114121436143614121337143614111437143614111437143614111437143614361412133714111411143615111411141213371411140005510001294914000d050000000000000000',
    'ext_on' : 0
}

tv = {

}

codes = {
    'light' : ceiling_light,
    'tv' : tv
}

devices = None

def send_ir_command(cmd_string):
    if (discover()):
        op, val = [ x.strip() for x in cmd_string.split(':') ]
        code = codes[op][val]
        if (code == 0): # extension code
            dispatch(op, val)
        else:
            send(code)
    else:
        print('no devices')

def discover():
    global devices
    if (devices is None):
        devices = broadlink.discover(timeout=5)
        devices[0].auth()
    return (devices is not None)

def dispatch(op, val):
    if (op == 'light'):
        light_ext(val)

def send(code):
    data = bytearray.fromhex(code)
    devices[0].send_data(data)

def light_ext(val):
    if (val == 'ext_on'):
        hour = datetime.now().time().hour
        print (hour)
        if (hour <= 6 or hour >= 18):
            val = 'fav'
        else:
            val = 'on'
        send(codes['light'][val])