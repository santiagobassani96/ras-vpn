# Simple vpn script

This script is meant to reboot my raspberry pi connection to openvpn server

`vpns.zip` contains a list of all possible servers with information

the `.env` file contains the user credentials

`mission_control` runs the basic loggic, at the moment it just try to connect to
any vpn server out there and keeps the connection alaive while it's working properly.


## CI workflow:
based on this [post](https://medium.com/@wkrzywiec/how-to-write-good-quality-python-code-with-github-actions-2f635a2ab09a)
