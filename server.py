import json
from flask import Flask,render_template,request,redirect,flash,url_for

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
        competition = [c for c in competitions if c['name'] == request.form['competition']][0]
        club = [c for c in clubs if c['name'] == request.form['club']][0]
        placesRequired = int(request.form['places'])
        competition['numberOfPlaces'] = str(int(competition['numberOfPlaces'])-placesRequired)
        club['points'] = str(int(club['points']) - placesRequired)
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions)

    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))

    return app
