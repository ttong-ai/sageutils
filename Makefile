.PHONY: lint test

test:
	black setup.py sageutils tests -l 115 --target-version py39 --check
	pytest --cov=./sageutils/ tests -v --disable-warnings

lint:
	black setup.py sageutils tests -l 115 --target-version py39
