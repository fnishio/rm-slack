# -*- coding: utf-8 -*-
from slackbot.bot import respond_to     # @botname in a channel/private channel chat
from slackbot.bot import listen_to      # channel/private channel chat
from libs import ir_code as ir
import re

@respond_to('send (.*)')
def send(message, command):
    #message.reply('accept command:' + command)
    commands = parse(command)
    for c in commands:
        ir.send_ir_command(c)

def parse(cmd_string):
    return [ x.strip() for x in cmd_string.split(',') ]