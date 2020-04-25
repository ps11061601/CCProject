install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

setup:
	python3 -m venv ~/.cloudproject

    
lint:
	hadolint Dockerfile 
	pylint --disable=R,C main.py
	pylint --disable=R,C locustfile.py
	pylint --disable=R,C python_scripts/**.py
	pylint --disable=R,C,W0104,E0602 wine_predict/**.ipynb

run:
	python3 main.py
	
all: 
	install lint test