run:
	FLASK_DEBUG=true FLASK_APP=server.py flask run

tests:
	pytest tests

unit-tests:
	pytest tests/units

acceptance-tests:
	pytest tests/acceptances
cov:
	coverage run -m pytest
	coverage report server.py

cov-html:
	coverage run -m pytest
	coverage html server.py


.PHONY: tests
