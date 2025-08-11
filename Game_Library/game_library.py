from flask import Flask, render_template, request, redirect, session, flash, url_for


class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console

game1 = Game('Tetris', 'Puzzle', 'Atari')
game2 = Game('God of War', 'Rack n Slash', 'PS2')
game3 = Game('Mortal Kombat', 'Fight', 'PS2')
games = [game1, game2, game3]

app = Flask(__name__)
app.secret_key = 'alura'

@app.route('/')
def index():
    return render_template('list.html', title = 'Games', games = games)

@app.route('/new-game')
def new_game():
    if 'username' not in session or session['username'] == None:
        return redirect(url_for('login', next = url_for('new_game')))

    return render_template('new_game.html', title = 'New Game')

@app.route('/create', methods=['POST', ])
def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    game = Game(name, category, console)

    games.append(game)

    return redirect(url_for('index'))

@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', next = next)

@app.route('/authenticate', methods=['POST', ])
def authenticate():
    if 'alohomora' == request.form['password']:
        session['username'] = request.form['username']
        flash(session['username'] + ' logged successfully!')
        next_page = request.form['next']
        return redirect(next_page)
    else:
        flash('User not logged in')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['username'] = None
    flash('Logout successfully!')
    return redirect(url_for('index'))

app.run(debug=True)