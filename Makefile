default: install install-dev

h help:
	@grep '^[a-z]' Makefile


install:
	pip install --upgrade pip
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

upgrade:
	pip install --upgrade pip
	pip install -r requirements.txt --upgrade
	pip install -r requirements-dev.txt --upgrade


fmt:
	black .


s serve:
	./water_dash/app.py
