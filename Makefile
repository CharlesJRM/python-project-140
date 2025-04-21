install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build --out-dir dist
	python setup.py sdist bdist_wheel

package-install:
	uv tool install dist/*.whl
	pip install dist/*.whl

lint:
	uv run ruff check brain_games

