#!/usr/bin/bash

# export PY_INSTALLED False

# command -v python3 >/dev/null 2>&1 && export $PY_INSTALLED True

# if [ $PY_INSTALLED == True ]; then
#     echo "[ + ]: python3 is installed"
# else
#     echo "[ - ]: python3 is not installed, please install it"
# fi

# does not work yet

pip install --upgrade pip
pip install pip-tools

pip-compile requirements.txt
# pip-compile
pip install -r requirements.txt

chmod +x ../main.py
chmod +x ./update.sh
chmod +x ./setup.sh