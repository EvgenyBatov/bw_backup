import dropbox
from datetime import datetime
import keyring


def upload(content):
    dropbox_token = keyring.get_password('dropbox', 'dropbox_token')
    dbx = dropbox.Dropbox(dropbox_token)
    file_name = '/{}.txt'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    dbx.files_upload(content, file_name)
