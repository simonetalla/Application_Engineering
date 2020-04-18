setup:
	python3 -m venv ~/.myrepo

install:
	# Install any needed plugins
	pip install --user --upgrade pip 
	pip install --user -r requirements.txt

test:
	# Run the Tests
	python -m pytest -vv --cov=my_library tests/*.py
	#python -m pytest --nbval notebook.ipynb


lint:
	pylint --disable=R,C my_library cli web

all: install lint test
