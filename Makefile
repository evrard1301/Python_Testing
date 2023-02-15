run:
	FLASK_DEBUG=true FLASK_APP=server.py flask run

unit-test:
	pytest

cov:
	coverage run -m pytest
	coverage report

