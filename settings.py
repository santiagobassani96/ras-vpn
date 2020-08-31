import os, sys
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


vpn_username = os.getenv('USERNAME')
vpn_password = os.getenv('PASSWORD')

CREDENTIALS_FILE = 'cred.up'

available_servers = [
    'za76.nordvpn.com.udp1194.ovpn'
]
