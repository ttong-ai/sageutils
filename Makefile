.PHONY: build lint test

build:
	python3 setup.py sdist bdist_wheel

test:
	black setup.py src tests -l 115 --target-version py39 --check
	pytest --cov=./src/ tests -v --disable-warnings

lint:
	black setup.py src tests -l 115 --target-version py39
