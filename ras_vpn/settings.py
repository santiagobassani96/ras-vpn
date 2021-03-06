import os
import sys

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


vpn_username = os.getenv("VPN_USERNAME")
vpn_password = os.getenv("VPN_PASSWORD")

CREDENTIALS_FILE = "cred.up"

VPN_PATH = "vpns"


TEST_URL = "https://drive.google.com/"
SLEEP_TIMER = 30 * 60  # 30 minutes
