export PY_INSTALLED False

command -v python3 >/dev/null 2>&1 && $PY_INSTALLED=True

if [ $PY_INSTALLED == True ]; then
    echo "[ + ]: python3 is installed"
else
    echo "[ - ]: python3 is not installed, please install it"
fi

pip install --upgrade pip
pip install pip-tools

pip-compile _requirements.txt
pip-compile