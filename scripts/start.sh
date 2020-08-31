#!/bin/bash

# launcher script which should be triggered by raspberry pi start up

# get the current path to this script, source:
# https://stackoverflow.com/questions/59895/how-to-get-the-source-directory-of-a-bash-script-from-within-the-script-itself
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd ${DIR}
cd ..
# now we are right at the root of the repo

# launch program
`python3 ras-vpn/mission_control.py`
