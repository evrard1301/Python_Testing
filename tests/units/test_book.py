def test_ok_book_find_club_and_competition(client, mocker):
    mocker.patch('server.clubs', new=[
        {
            'name': 'myclub',
            'email': 'hello@world.com',
            'places': 5
        }
    ])

    mocker.patch('server.competitions', new=[
        {
            'name': 'mycompetition',
            'date': '2023-10-22 13:30:00',
            'numberOfPlaces': '15'
        }
    ])
    
    response = client.get('/book/mycompetition/myclub')
    assert 200 == response.status_code
    

def test_err_book_club_not_found(client, mocker):
    mocker.patch('server.clubs', new=[])

    mocker.patch('server.competitions', new=[
        {
            'name': 'mycompetition',
            'date': '2023-10-22 13:30:00',
            'numberOfPlaces': '15'
        }
    ])
    
    response = client.get('/book/mycompetition/myclub')
    assert 404 == response.status_code
    

def test_err_book_competition_not_found(client, mocker):
    mocker.patch('server.clubs', new=[
        {
            'name': 'myclub',
            'email': 'hello@world.com',
            'places': 5
        }
    ])

    mocker.patch('server.competitions', new=[])
    
    response = client.get('/book/mycompetition/myclub')
    assert 404 == response.status_code
