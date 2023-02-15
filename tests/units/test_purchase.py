import server

def test_ok_purchase(client, mocker):

    mocker.patch('server.clubs', new=[
        {
            'name': 'myclub',
            'email': 'hello@world.com',
            'points': '7'
        }
    ])

    mocker.patch('server.competitions', new=[
        {
            'name': 'mycompetition',
            'date': '2023-10-22 13:30:00',
            'numberOfPlaces': '15'
        }
    ])
    
    client.post('/purchasePlaces', data={
        'competition': 'mycompetition',
        'club': 'myclub',
        'places': '5'
    })
    
    assert '10' == server.competitions[0]['numberOfPlaces']
    assert '2' == server.clubs[0]['points']

def test_err_purchase_no_club(client, mocker):

    mocker.patch('server.clubs', new=[])

    mocker.patch('server.competitions', new=[
        {
            'name': 'mycompetition',
            'date': '2023-10-22 13:30:00',
            'numberOfPlaces': '15'
        }
    ])
    
    response = client.post('/purchasePlaces', data={
        'competition': 'mycompetition',
        'club': 'myclub',
        'places': '5'
    })

    assert 404 == response.status_code

def test_err_purchase_no_competition(client, mocker):

    mocker.patch('server.clubs', new=[
        {
            'name': 'myclub',
            'email': 'hello@world.com',
            'points': '7'
        }
    ])

    mocker.patch('server.competitions', new=[])
    
    response = client.post('/purchasePlaces', data={
        'competition': 'mycompetition',
        'club': 'myclub',
        'places': '5'
    })

    assert 404 == response.status_code

def test_err_purchase_no_enough_points(client, mocker):

    mocker.patch('server.clubs', new=[
        {
            'name': 'myclub',
            'email': 'hello@world.com',
            'points': '5'
        }
    ])

    mocker.patch('server.competitions', new=[
        {
            'name': 'mycompetition',
            'date': '2023-10-22 13:30:00',
            'numberOfPlaces': '15'
        }
    ])
    
    client.post('/purchasePlaces', data={
        'competition': 'mycompetition',
        'club': 'myclub',
        'places': '6'
    })
    
    assert '15' == server.competitions[0]['numberOfPlaces']
    assert '5' == server.clubs[0]['points']

def test_err_purchase_no_enough_places(client, mocker):

    mocker.patch('server.clubs', new=[
        {
            'name': 'myclub',
            'email': 'hello@world.com',
            'points': '5'
        }
    ])

    mocker.patch('server.competitions', new=[
        {
            'name': 'mycompetition',
            'date': '2023-10-22 13:30:00',
            'numberOfPlaces': '1'
        }
    ])
    
    client.post('/purchasePlaces', data={
        'competition': 'mycompetition',
        'club': 'myclub',
        'places': '2'
    })
    
    assert '1' == server.competitions[0]['numberOfPlaces']
    assert '5' == server.clubs[0]['points']
