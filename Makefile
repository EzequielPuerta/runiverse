freeze:
	cd backend && pip freeze > requirements.txt

runserver:
	cd backend && python3 manage.py runserver

pre-commit-install:
	cd backend && pre-commit install

pre-commit-autoupdate:
	cd backend && pre-commit autoupdate

pre-commit-run:
	cd backend && pre-commit run --all-files
