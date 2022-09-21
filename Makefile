install:
		poetry install


gendiff:
		poetry run gendiff


build:
		poetry build


publish:
		poetry publish --dry-run


package-install:
		python3 -m pip install --user --force dist/*.whl


test:
		poetry run pytest


test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/


make lint:
		poetry run flake8 gendiff
