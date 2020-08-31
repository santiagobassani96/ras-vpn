# Simple vpn script

This script is meant to reboot my raspberry pi connection to openvpn server

`vpns.zip` contains a list of all possible servers with information

we use `env vars` to set `username` and `password` for the vpn client.

`vpn_tools` runs the basic loggic, at the moment it just try to connect to
any vpn server out there and keeps the connection alaive while it's working properly.

## How to run:
- Download repo
- `cd ras-vpn`
- Set `export VPN_USERNAME=...` `export VPN_PASSWORD=...`
- `bash scripts/start.sh`
- Check for status in the `log.txt` file


## CI workflow:
based on this [post](https://medium.com/@wkrzywiec/how-to-write-good-quality-python-code-with-github-actions-2f635a2ab09a)
