from pytest_bdd import scenarios, given, when, then, parsers
from bs4 import BeautifulSoup

scenarios('features/public_board.feature')

@given(parsers.parse('le club \'{name}\' ayant {points} points'))
def given_club(context, name, points):
    context[name] = points

@when(parsers.parse('je réserve {places} places pour \'{clubname}\''))
def when_purchase(context, client, mocker, places, clubname, tomorrow):

    clubs = mocker.patch('server.clubs', new=[
        {
            'name': clubname,
            'email': f'{clubname}@email.com',
            'points': context[clubname]
        }
    ])

    mocker.patch('server.competitions', new=[
        {
            'name': 'mycompetition',
            'date': tomorrow,
            'numberOfPlaces': str(int(places) * 2)
        }
    ])

    client.post('/purchasePlaces', data={
        'club': clubname,
        'competition': 'mycompetition',
        'places': places
    })

    context[clubname] = clubs[0]['points']

@when('je consulte le tableau de points')
def when_consult(context, client, mocker):
    clubs = []
    for club in context.keys():
        clubs.append({
            'name': club,
            'email': f'{club}@email.com',
            'points': context[club]
        })

    mocker.patch('server.clubs', new=clubs)
    
    html = client.get('/publicBoard').data.decode('utf-8')
    context['html'] = BeautifulSoup(html, 'html.parser')
    
    
@then(parsers.parse('je vois dans le tableau que \'{clubname}\' a {points} points'))
def then_lookat_board(context, clubname, points):
    html = context['html']
    all_clubs = []
    all_points = []
    
    for td in html.findAll('td'):
        if all(t.isdigit() for t in td.text):
            all_points.append(td.text)
        else:
            all_clubs.append(td.text)
            
    assert clubname in all_clubs
    assert points == all_points[all_clubs.index(clubname)]
