# dummy file for now
# the import problem was solved formm:
# https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
import os
import sys

test_module_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, test_module_path + "/../")

from ras_vpn.vpn_tools import test_connection


def test_test_connection():
    return test_connection()
