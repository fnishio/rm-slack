# Install libraries
pip3 install slackbot
pip3 install broadlink

# Setup configuration file
Copy slackbot_settings.py.template to slackbot_settings.py, and put your slack API token.

# Slackbot IR command

Setup IFTTT applet using the following IR commands.

|Command|Device|IR command|Description    |
|:------|:-----|:---------|:--------------|
|send   |light |on      | on/off toggle |
|       |      |bright  | brighter      |
|       |      |dark    | darker        |
|       |tv    |power   | on/off toggle |
|       |      |1-12    |channel        |
|       |      |t       |Telestrial     |
|       |      |bs      |BS             |
|       |      |cs      |CS             |
|       |      |vol_up  |volume up      |
|       |      |vol_down|volume down    |
|       |      |vol_mute|volume mute    |
|       |      |ch_up   |channel up     |
|       |      |ch_down |channel down   |
|       |audio |power   |on/off toggle  |
|       |      |vol_up  |volume up      |
|       |      |vol_down|volume down    |
|       |      |prev    |prev track     |
|       |      |next    |next track     |

# IR codes
Learn IR codes of  your devices, and put those into ir_code.py.