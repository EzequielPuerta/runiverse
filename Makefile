freeze:
	cd backend && pip freeze > requirements.txt

runserver:
	cd backend && python3 manage.py runserver
