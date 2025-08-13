from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from game_library import app, db
from models import Games
from helpers import recover_image, delete_image, GameForm
import time

@app.route('/')
def index():
    games_list = Games.query.order_by(Games.id)
    game_covers = [recover_image(game.id) for game in games_list]

    games_with_covers = list(zip(games_list, game_covers))
    return render_template('list.html', title = 'Games', games_with_covers = games_with_covers)

@app.route('/new-game')
def new_game():
    if 'username' not in session or session['user_logged'] == None:
        return redirect(url_for('login', next = url_for('new_game')))

    form = GameForm()
    return render_template('new_game.html', title = 'New Game', form = form)

@app.route('/create', methods=['POST', ])
def create():
    form = GameForm(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('new_game'))

    name = form.name.data
    category = form.category.data
    console = form.console.data

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
        return redirect(url_for('login', next = url_for('edit', id = id)))

    game = Games.query.filter_by(id = id).first()
    form = GameForm()
    form.name.data = game.name
    form.category.data = game.category
    form.console.data = game.console

    game_cover = recover_image(id)
    return render_template('edit.html', title = 'Editing Game', id = id, game_cover = game_cover, form = form)

@app.route('/update', methods=['POST', ])
def update():
    form = GameForm(request.form)
    if form.validate_on_submit():
        game = Games.query.filter_by(id = request.form['id']).first()
        game.name = form.name.data
        game.category = form.category.data
        game.console = form.console.data

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

@app.route('/uploads/<archive_name>')
def image(archive_name):
    return send_from_directory('uploads', archive_name)