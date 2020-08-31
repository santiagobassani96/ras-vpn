import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

import logging
import random
import shutil
import time
import zipfile

import requests
from settings import CREDENTIALS_FILE, VPN_PATH, vpn_password, vpn_username

"""
This script aims to solve my anoying internet problem. By susbcribing a 
service which could potentially restart as many times as it needs
"""

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="log.txt",
)


test_url = "https://drive.google.com/"
sleep_timer = 30 * 60  # 30 minutes

vpns = "vpns"


def add_credentials(vpns: [str], cred_path: str):
    """
    Add credentials file path to each and every vpn config file.
    """
    # first we set the cred file as default auth file
    for config_file in os.listdir(vpns):
        with open(vpns + "/" + config_file, "r+") as f:
            content = f.read()
            if content.find(cred_path) != -1:
                continue
            f.seek(0)
            content = content.replace(
                "auth-user-pass", "auth-user-pass {}".format(cred_path)
            )
            f.write(content)
            f.truncate()


def update_cred_file(user: str, password: str) -> str:
    """
    Create or update credentials file with new credentials:
    The file keep user password format (user/npassword/n)
    Params:
        - user: str
        - passord: str

    Returns:
        - str: name of the file or none if something fails

    """
    try:
        with open(CREDENTIALS_FILE, "w") as f:
            cred = "{}\n{}\n".format(user, password)
            f.write(cred)
        return CREDENTIALS_FILE
    except Exception as e:
        logging.error(str(e))
        return None


def test_connection():
    """
    Test internet connection until failure
    """
    resp = requests.get(test_url)
    if resp.status_code == 200:
        return True
    else:
        return False


def main():
    # if uncompressed, erased old folder
    try:
        shutil.rmtree(VPN_PATH + ".zip")
    except Exception as e:
        # this means, it wasn't uncompressed
        pass

    # uncompress vpn zipfile
    # this will leave a folder 'vpns' with all config ovpns files
    with open(VPN_PATH + ".zip", "f") as f:
        zipfile.ZipFile(f).extractall()

    update_cred_file(vpn_username, vpn_password)

    # first we add credentials to each file
    add_credentials(vpns, CREDENTIALS_FILE)
    # next we try to connect
    while True:
        try:
            vpn = random.choice(os.listdir(vpns))
            logging.info("trying to connect to {}".format(vpn))
            res = os.system("sudo openvpn {}".format(os.path.join(vpns, vpn)))
            logging.info("result was {}".format(res))
            while test_connection():
                # try internet connection
                # this method raises an exception which
                # ends the cicle and changes the vpn connection.
                logging.info("spleeing for 30 min")
                time.sleep(sleep_timer)

            return res
        except Exception as e:
            logging.error("there was an error")


if __name__ == "__main__":
    main()
