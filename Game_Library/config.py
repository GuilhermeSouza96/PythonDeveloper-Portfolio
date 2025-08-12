import os

SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = '{SGBD}://{user}:{password}@{localhost}/{database}'.format(
    SGBD = 'mysql+mysqlconnector',
    user = 'root',
    password = 'admin',
    localhost = 'localhost',
    database = 'game_library'
)

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'