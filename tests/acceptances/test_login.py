from pytest_bdd import scenarios, given, when, then, parsers
from tests.acceptances.common import *

scenarios('features/login.feature')

@given(parsers.parse('mon adresse email est \'{email}\''))
def given_email(context, email):
    context['myemail'] = email

@when(parsers.parse('je me connecte avec \'{email}\''))
def user_connect(context, client, email, mocker):

    mocker.patch('server.clubs', new=[
        {
            'name': 'myclub',
            'email': context['myemail'],
            'points': '100'
        }
    ])

    context['response'] = client.post('/showSummary', data={
        'email': email
    })
    
    assert True
