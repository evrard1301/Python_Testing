def test_ok_summary_email_found(app, client, mocker):
    mocker.patch('server.clubs', new=[
            {
                'name': 'my club',
                'email': 'hello@world.com',
                'points': '12'
            }
    ])

    response = client.post('/showSummary', data={
        'email': 'hello@world.com'
    })

    assert 200 == response.status_code


def test_ok_summary_email_not_found(app, client, mocker):
    mocker.patch('server.clubs', new=[
            {
                'name': 'my club',
                'email': 'hello2@world.com',
                'points': '12'
            }
    ])

    response = client.post('/showSummary', data={
        'email': 'hello@world.com'
    })

    assert 401 == response.status_code
