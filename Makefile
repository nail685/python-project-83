PORT ?= 8000
start:
	uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

start2:
	waitress-serve --listen=127.0.0.1:$(PORT) page_analyzer:app

render-start:
	gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

install:
	uv sync

dev:
	uv run flask --debug --app page_analyzer:app run

lint:
	uv run ruff check page_analyzer

build:
	./build.sh

test-coverage:
	uv run pytest --cov=page_analyzer --cov-report xml