from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from models import db, Game
from admin import admin, GameAdminView
from brain_games.games import brain_calc, brain_even, brain_gcd, brain_prime, brain_progression

games = {
    "brain_calc": brain_calc,
    "brain_even": brain_even,
    "brain_gcd": brain_gcd,
    "brain_prime": brain_prime,
    "brain_progression": brain_progression,
}

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
admin.init_app(app)

# Добавляем GameAdminView к admin здесь, чтобы избежать циклических импортов
admin.add_view(GameAdminView(Game, session=db.session))


@app.route('/', methods=['GET', 'POST'])
def index():
    games = Game.query.all()
    return render_template('index.html', games=games)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
