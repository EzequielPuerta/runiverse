.PHONY: init run-all runserver run-app run-admin start \
		django-makemigrations django-migrate \
		alembic-init alembic-makemigrations alembic-migrate freeze \
		poetry-install poetry-add poetry-remove pre-commit-install \
		pre-commit-autoupdate pre-commit-run

##################################################
# Initialization
##################################################
init:
	$(MAKE) poetry-install
	$(MAKE) pre-commit-install
	$(MAKE) pre-commit-autoupdate
	$(MAKE) alembic-init
	$(MAKE) django-migrate

##################################################
# Running
##################################################
run-all:
	$(MAKE) runserver & \
	$(MAKE) run-app & \
	$(MAKE) run-admin & \
	wait

stop-all:
	pkill -f 'manage.py runserver' && pkill -f 'pnpm dev'

run-app:
	cd app && pnpm run dev -- --port 5173

run-admin:
	cd admin && pnpm run dev -- --port 5174

##################################################
# Django
##################################################
runserver:
	cd backend && poetry run python manage.py runserver

start:
	cd backend && poetry run python manage.py startapp $(app)

django-makemigrations:
	cd backend && poetry run python manage.py makemigrations

django-migrate:
	cd backend && poetry run python manage.py migrate

##################################################
# Alembic
##################################################
alembic-init:
	cd backend && poetry run alembic init alembic

alembic-makemigrations:
	cd backend && poetry run alembic revision --autogenerate -m "$(msg)"

alembic-migrate:
	cd backend && poetry run alembic upgrade head

##################################################
# Pip
##################################################
freeze:
	cd backend && poetry export --without-hashes --format=requirements.txt > runiverse/requirements.txt

##################################################
# Poetry
##################################################
poetry-install:
	cd backend && poetry install

poetry-add:
	cd backend && poetry add $(if $(dev),--group dev,) $(pkg)
	$(MAKE) freeze

poetry-remove:
	cd backend && poetry remove $(pkg)
	$(MAKE) freeze

##################################################
# Pre-Commit
##################################################
pre-commit-install:
	cd backend && poetry run pre-commit install

pre-commit-autoupdate:
	cd backend && poetry run pre-commit autoupdate

pre-commit-run:
	cd backend && poetry run pre-commit run --all-files
