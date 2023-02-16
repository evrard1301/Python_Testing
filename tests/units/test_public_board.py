def test_public_board_exists(client):
    response = client.get('/publicBoard')
    assert 200 == response.status_code
