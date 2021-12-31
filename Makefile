
arch:
	sudo pacman -S python3
	sudo pacman -S --overwrite="*" python-pip python-setuptools python-pyqt5
	sudo pacman -S pyqt5
	
	python -m venv nscalc
	source nscalc/bin/activate && pip install pybuilder
	pyb