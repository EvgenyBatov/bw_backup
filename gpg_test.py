from subprocess import Popen, PIPE


def encrypt(raw_bytes, passphrase):
    # todo not secure as passphrase appears in ps output
    p = Popen(['gpg', '--symmetric', '--cipher-algo', 'AES256', '--batch', '--passphrase', passphrase], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    encrypted_bytes = p.communicate(input=raw_bytes)[0]
    return encrypted_bytes


def decrypt(encrypted_bytes, passphrase):
    # todo not secure as passphrase appears in ps output
    p = Popen(['gpg', '--cipher-algo', 'AES256', '--batch', '--passphrase', passphrase], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    decrypted_bytes = p.communicate(input=encrypted_bytes)[0]
    return decrypted_bytes


data = 'test_data'
passphrase = 'qwerty'
encrypted_data = encrypt(data.encode(), passphrase)
decrypted_data = decrypt(encrypted_data, passphrase)
print(decrypted_data.decode())
