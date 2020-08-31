import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

import logging
import random
import shutil
import time
from zipfile import ZipFile

import requests

from .settings import (
    CREDENTIALS_FILE,
    SLEEP_TIMER,
    TEST_URL,
    VPN_PATH,
    vpn_password,
    vpn_username,
)

"""
This script aims to solve my anoying internet problem. By susbcribing a 
service which could potentially restart as many times as it needs
"""


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
    resp = requests.get(TEST_URL)
    if resp.status_code == 200:
        return True
    else:
        return False


def connect():
    # if uncompressed, erased old folder
    try:
        shutil.rmtree(VPN_PATH + ".zip")
    except Exception as e:
        # this means, it wasn't uncompressed
        pass

    # uncompress vpn zipfile
    # this will leave a folder 'vpns' with all config ovpns files

    ZipFile(VPN_PATH + ".zip").extractall()

    update_cred_file(vpn_username, vpn_password)

    # first we add credentials to each file
    add_credentials(VPN_PATH, CREDENTIALS_FILE)
    # next we try to connect
    while True:
        try:
            vpn = random.choice(os.listdir(VPN_PATH))
            logging.info("trying to connect to {}".format(vpn))
            res = os.system("sudo openvpn {}".format(os.path.join(VPN_PATH, vpn)))
            logging.info("result was {}".format(res))
            while test_connection():
                # try internet connection
                # this method raises an exception which
                # ends the cicle and changes the vpn connection.
                logging.info("sleeping for 30 min")
                time.sleep(SLEEP_TIMER)

            return res
        except Exception as e:
            logging.error("there was an error")
