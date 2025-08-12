from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from game_library import app, db
from models import Games, Users
from helpers import recover_image, delete_image
import time

@app.route('/')
def index():
    games_list = Games.query.order_by(Games.id)
    return render_template('list.html', title = 'Games', games = games_list)

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

    game = Games.query.filter_by(name = name).first()

    if game:
        flash('Game already exists')
        return redirect(url_for('index'))

    new_game = Games(name = name, category = category, console = console)
    db.session.add(new_game)
    db.session.commit()

    archive = request.files['archive']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    archive.save(f'{upload_path}/cover-{new_game.id}-{timestamp}.jpg')

    return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
    if 'username' not in session or session['username'] == None:
        return redirect(url_for('login', next = url_for('edit')))

    game = Games.query.filter_by(id = id).first()
    game_cover = recover_image(id)
    return render_template('edit.html', title = 'Editing Game', game = game, game_cover = game_cover)

@app.route('/update', methods=['POST', ])
def update():
    game = Games.query.filter_by(id = request.form['id']).first()
    game.name = request.form['name']
    game.category = request.form['category']
    game.console = request.form['console']

    db.session.add(game)
    db.session.commit()

    archive = request.files['archive']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    delete_image(game.id)
    archive.save(f'{upload_path}/cover-{game.id}-{timestamp}.jpg')

    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    if 'username' not in session or session['username'] == None:
        return redirect(url_for('login'))

    Games.query.filter_by(id = id).delete()

    db.session.commit()
    flash('Game was deleted!')
    return redirect(url_for('index'))



@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', next = next)

@app.route('/authenticate', methods=['POST', ])
def authenticate():
    user = Users.query.filter_by(nickname = request.form['username']).first()
    if user:
        if request.form['password'] == user.password:
            session['username'] = user.nickname
            flash(user.nickname + ' logged successfully!')
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

@app.route('/uploads/<archive_name>')
def image(archive_name):
    return send_from_directory('uploads', archive_name)


