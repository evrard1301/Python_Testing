from pytest_bdd import scenarios, given, when, then, parsers

scenarios('features/purchase.feature')


@given(parsers.parse('mon club ayant {points} points'))
def given_a_club(mocker, context, points):
    context['current_clubs'] = mocker.patch('server.clubs', new=[
        {
            'name': 'myclub',
            'email': 'myclub@email.com',
            'points': points
        }
    ])


@given(parsers.parse('la compétition se déroule le \'{date}\''))
def given_the_competition_is_over(mocker, context, date):
    context['current_competitions'][0]['date'] = date


@given(parsers.parse('une compétition ayant {places} places'))
def given_a_competition(mocker, context, places):
    context['current_competitions'] = mocker.patch('server.competitions', new=[
        {
            'name': 'mycompetition',
            'date': '2090-10-22 13:30:00',
            'numberOfPlaces': places
        }
    ])


@when(parsers.parse('je réserve {places} places'))
def when_purchasing(mocker, context, client, places):

    mocker.patch('server.clubs', new=context['current_clubs'])
    mocker.patch('server.competitions', new=context['current_competitions'])

    context['response'] = client.post('/purchasePlaces', data={
        'club': 'myclub',
        'competition': 'mycompetition',
        'places': places
    })


@then(parsers.parse('il me reste {rem_points} points'))
@then(parsers.parse('il me reste {rem_points} point'))
def then_remaining(context, mocker, rem_points):
    assert rem_points == context['current_clubs'][0]['points']


@then(parsers.parse('il reste {rem_places} places à la compétition'))
@then(parsers.parse('il reste {rem_places} place à la compétition'))
def then_remaining_competition(context, rem_places):
    assert rem_places == context['current_competitions'][0]['numberOfPlaces']
