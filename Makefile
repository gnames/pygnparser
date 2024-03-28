all: build install

.PHONY: build install test distclean dist up

build:
	python setup.py build

install: build
	pip install .

test:
	pytest --cov-report term --cov=pygnparser test/

check:
	python -m twine check dist/*

distclean:
	rm dist/*

dist:
	python setup.py sdist bdist_wheel --universal

up:
	python -m twine upload dist/*

uptest:
	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*