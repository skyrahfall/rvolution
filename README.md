# rvolution
A Python wrapper to remote control  R_Volution media Player via API
You can send most commands from your remote control via API.




# Installation
`pip install rvolution`

## Usage

### send Play/Pause
```
from rvolution import RVolutionPlayer

player = RVolutionPlayer('192.168.178.98')

status = player.send_button('Play / Pause')
```

### get current status
get the current status of the player
```
status = player.update_state()
```

### supported commands
you can also retrieve a list of supported remote control buttons

```
player = supported_buttons()
```


# Limitations

## Power On/off
Power on command only works, when your players power button is configured to "Video output off".
If it is set to "Power off" the API is not working.
I also tried using WakeOnLan but without success.

## limited test devices
I only can test it with my R_Volution PlayerOne 8K.