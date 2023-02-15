def test_ok_index(app, client):
    assert 200 == client.get('/').status_code
