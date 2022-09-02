install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=brain_games --cov-report xml

lint:
	poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck test lint

build:
	poetry build
	
publish:
	publish --dry-run
	
package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

brain-even:
	poetry run brain-even

.PHONY: install test lint selfcheck check build