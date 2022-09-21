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


make lint:
		poetry run flake8 gendiff


make test-coverage:
		pytest --cov=tests
