import os
from game_library import app

def recover_image(id):
    for archive_name in os.listdir(app.config['UPLOAD_PATH']):
        if f'cover-{id}' in archive_name:
            return archive_name

    return 'capa-padrao.jpg'

def delete_image(id):
    archive = recover_image(id)
    if archive != 'capa-padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], archive))