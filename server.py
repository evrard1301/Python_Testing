import json
import datetime
from flask import Flask,render_template,request,redirect,flash,url_for

class PurchaseManager:

    class Purchase:
        def __init__(self, club, competition, places):
            self.club = club
            self.competition = competition
            self.places = places

    def __init__(self):
        self.purchases = []

    def get(self, club, competition):
        all_p = [
            p
            for p in self.purchases
            if p.club == club
            and p.competition == competition
        ]

        if len(all_p) == 0:
            return 0
        
        return all_p[0].places
        
        
    def update(self, club, competition, places):
        all_p = [
            p
            for p in self.purchases
            if p.club == club
            and p.competition == competition
        ]

        if len(all_p) == 0:
            self.purchases.append(self.Purchase(club,
                                                competition,
                                                places))
        else:
            all_p[0].places += places
        
def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions
    
competitions = []
clubs = []
purchase_manager = PurchaseManager()
    
def create_app():
    app = Flask(__name__)
    app.secret_key = 'something_special'
    
    global competitions
    global clubs

    competitions = loadCompetitions()
    clubs = loadClubs()

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/showSummary',methods=['POST'])
    def showSummary():
        all_clubs = [club for club in clubs if club['email'] == request.form['email']]

        if len(all_clubs) > 0:
            club = all_clubs[0]
            return render_template('welcome.html',club=club,competitions=competitions)
        flash('wrong credentials')
        return render_template('index.html'), 401


    @app.route('/book/<competition>/<club>')
    def book(competition,club):
        foundClubs = [c for c in clubs if c['name'] == club]
        foundCompetitions = [c for c in competitions if c['name'] == competition]
        
        if len(foundClubs) > 0 and len(foundCompetitions) > 0:
            return render_template('booking.html',
                                   club=foundClubs[0],
                                   competition=foundCompetitions[0])
        else:
            flash("Something went wrong-please try again")
            return render_template('welcome.html', club=club, competitions=competitions), 404


    @app.route('/purchasePlaces',methods=['POST'])
    def purchasePlaces():
        my_competitions = [c for c in competitions if c['name'] == request.form['competition']]
        my_clubs = [c for c in clubs if c['name'] == request.form['club']]

        if len(my_competitions) == 0 or len(my_clubs) == 0:
            return render_template('index.html'), 404
        club = my_clubs[0]
        competition = my_competitions[0]
        competition_date = datetime.datetime.strptime(competition['date'],
                                                      '%Y-%m-%d %H:%M:%S')
        current_date = datetime.datetime.now()

        placesRequired = int(request.form['places'])

        previousRequired = purchase_manager.get(club,
                                                competition)
        
        if competition_date < current_date:
            flash('cannot purchase a terminated competition')
            return render_template('welcome.html', club=club, competitions=competitions)

        if placesRequired + previousRequired > 12:
            flash('cannot purchase more than'
                  ' 12 places by competition')
            return render_template('welcome.html', club=club, competitions=competitions)

        if placesRequired > int(club['points']):
            flash('not enough point')
            return render_template('welcome.html', club=club, competitions=competitions)

        if placesRequired > int(competition['numberOfPlaces']):
            flash('not enough places')
            return render_template('welcome.html', club=club, competitions=competitions)

        competition['numberOfPlaces'] = str(int(competition['numberOfPlaces'])-placesRequired)
        club['points'] = str(int(club['points']) - placesRequired)
        purchase_manager.update(club,
                                competition,
                                placesRequired)
        
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions)

    @app.route('/publicBoard')
    def public_board():
        return render_template('board.html', clubs=clubs)
    
    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))
    
    return app
