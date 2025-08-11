from flask import Flask, render_template, request, redirect


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

@app.route('/')
def index():
    return render_template('list.html', title = 'Games', games = games)

@app.route('/new-game')
def new_game():
    return render_template('new_game.html', title = 'New Game')

@app.route('/create', methods=['POST', ])
def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    game = Game(name, category, console)

    games.append(game)

    return redirect('/')

app.run(debug=True)