import os
from game_library import app
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField


class GameForm(FlaskForm):
    name = StringField('Game Name', [validators.DataRequired(), validators.Length(min=1, max=50)])
    category = StringField('Category', [validators.DataRequired(), validators.Length(min=1, max=40)])
    console = StringField('Console', [validators.DataRequired(), validators.Length(min=1, max=20)])
    save = SubmitField('Save Game')

class UserForm(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=15)])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')

def recover_image(id):
    for archive_name in os.listdir(app.config['UPLOAD_PATH']):
        if f'cover-{id}' in archive_name:
            return archive_name

    return 'capa-padrao.jpg'

def delete_image(id):
    archive = recover_image(id)
    if archive != 'capa-padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], archive))