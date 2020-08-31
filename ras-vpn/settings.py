import os
import sys

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


vpn_username = os.getenv("USERNAME")
vpn_password = os.getenv("PASSWORD")

CREDENTIALS_FILE = "cred.up"

VPN_PATH = "vpns"
