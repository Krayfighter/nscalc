
test:
	python3 main.py

dist:
	echo "not yet implemented"

arch:
	pacman --version
	sudo pacman -S python3
	sudo pacman -S --overwrite="*" python-pip python-setuptools python-pyqt5
	sudo pacman -S pyqt5
	pip install --upgrade pip
	pip install pip-tools

# deb:
# 	apt --version
# 	sudo apt install python3
# 	python3 -m pip install --upgrade-pip