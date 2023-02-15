run:
	FLASK_DEBUG=true FLASK_APP=server.py flask run

unit-test:
	pytest
