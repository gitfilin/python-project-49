install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

build:
	poetry build

publish:
	poetry publish --dry-run

make lint:
	poetry run flake8 brain_games

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=brain_games --cov-report xml
