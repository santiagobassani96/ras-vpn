#!/bin/bash

# format and checks pythn code usign balck and isort
# get the current path to this script, source:
# https://stackoverflow.com/questions/59895/how-to-get-the-source-directory-of-a-bash-script-from-within-the-script-itself
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd ${DIR}
cd ..

`isort ras_vpn`
`black ras_vpn`

# also check for main file

`isort mission_control.py`
`black mission_control.py`

# finally analyze test folder

`isort test`
`black test`
