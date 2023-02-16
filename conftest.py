import pytest
import datetime
from server import create_app

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def tomorrow():
    date = datetime.datetime.now() + datetime.timedelta(days=1)
    return date.strftime('%Y-%m-%d %H:%M:%S')

@pytest.fixture(scope='module')
def context():
    return {}
