import keyring

from bw_wrapper import BwWrapper
import dropbox_api as dbx
import encryption

credential = keyring.get_credential("bw_backup", None)
username = credential.username
password = credential.password
bw = BwWrapper()
try:
    bw.login(username, password)
    bw.sync()
    backup = bw.list_items()
    encrypted_backup = encryption.password_encrypt(backup, password)
    dbx.upload(encrypted_backup)
finally:
    bw.logout()
