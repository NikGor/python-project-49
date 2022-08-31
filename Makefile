install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 hexlet_python_package

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build
	
publish:
	publish --dry-run
	
package-install:
	python3 -m pip install --user dist/*.whl

brain-games:
	poetry run brain-games

.PHONY: install test lint selfcheck check build