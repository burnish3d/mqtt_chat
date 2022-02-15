setup: requirements_dev.txt
	python3 -m pip install requirements_dev.txt 

clean:
	rm -rf build
	rm -rf dist
	rm -rf __pycache__

venv: venv/bin/activate 
	source venv/bin/activate

venv/bin/activate: requirements_dev.txt
	python3 -m venv venv
	./venv/bin/python3 -m pip install -r requirements_dev.txt

build: clean
	python3 -m setup sdist bdist_wheel

token_location = over_ride_this_value_manually
token = `cat $(token_location)`
#we only need to use those values if we do not have a .pypirc file
distribute:
	python3 -m twine upload dist/*
#	python3 -m twine upload -u __token__ -p $(token) dist/*

test_token_location = over_ride_this_value_manually
test_token = `cat $(test_token_location)`
distribute-test:
	python3 -m twine upload --repository testpypi -u __token__ -p $(test_token)  dist/*