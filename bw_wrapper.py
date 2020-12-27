import re
import subprocess
import pexpect

class BwWrapper():
    def __init__(self):
        self.session_id = None

    def login(self, username, password):
        #result = subprocess.run(["bw", "login", username, password], stdout=subprocess.PIPE)
        #output = result.stdout.decode("utf-8")
        process = pexpect.spawn('bw login')
        process.expect('Email address:')
        process.sendline(username)
        process.expect('Master password:')
        process.sendline(password)
        output = process.read().decode("utf-8")
        if 'You are logged in!' in output:
            self.session_id = re.search('BW_SESSION="(.+)"', output).group(1)
            return
        if 'You are already logged in as' not in output:
            raise Exception('Failed to login')

    def logout(self):
        subprocess.run(["bw", "logout"], stdout=subprocess.DEVNULL)
        # You have logged out.

    def list_items(self):
        result = subprocess.run(['bw', 'list', 'items', '--session', self.session_id], stdout=subprocess.PIPE)
        return result.stdout
