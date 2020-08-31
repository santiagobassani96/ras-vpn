# Simple vpn script
[![codecov](https://codecov.io/gh/santiagobassani96/ras-vpn/branch/master/graph/badge.svg)](https://codecov.io/gh/santiagobassani96/ras-vpn)

This script is meant to reboot my raspberry pi connection to openvpn server

`vpns.zip` contains a list of all possible servers with information

we use `env vars` to set `username` and `password` for the vpn client.

`vpn_tools` runs the basic loggic, at the moment it just try to connect to
any vpn server out there and keeps the connection alaive while it's working properly.

## How to run:
### Manul execution
- Download repo
- `cd ras-vpn`
- Set `export VPN_USERNAME=...` `export VPN_PASSWORD=...`
- `bash scripts/start.sh`
- Check for status in the `log.txt` file

### Set a chron job
- Download repo
- `cd ras-vpn`
- Set `export VPN_USERNAME=...` `export VPN_PASSWORD=...`
- `sudo crontab -e`

- `@reboot sh /path/to/repo/scripts/start.sh > /home/pi/logs/cronlog 2>&1` 

What this does is rather than executing the launcher script at a specific time, it will execute it once upon startup

this is based on the follwoing [post](https://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/)

## CI workflow:
based on this [post](https://medium.com/@wkrzywiec/how-to-write-good-quality-python-code-with-github-actions-2f635a2ab09a)

## Tools:
- `python 3.8`
- `virtualenv`
- `pipreqs`
- `black`
- `isort`
- `flake8`
- `pytest`
