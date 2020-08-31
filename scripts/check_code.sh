#!/bin/bash

# format and checks pythn code usign balck and isort
# get the current path to this script, source:
# https://stackoverflow.com/questions/59895/how-to-get-the-source-directory-of-a-bash-script-from-within-the-script-itself
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd ${DIR}
cd ..

`isort ras-vpn`
`black ras-vpn`
