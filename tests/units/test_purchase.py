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
