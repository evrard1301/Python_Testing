def test_ok_logout(app, client):
    assert 302 == client.get('/logout').status_code
