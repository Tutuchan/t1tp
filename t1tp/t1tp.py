#!/usr/bin/env python

import os
import subprocess
import json
import sys
from pathlib import Path
from datetime import datetime
from datetime import timedelta


class OnePassword:
    _token_path = os.path.join(Path.home(), ".op", "token")

    def __init__(self):

        if not self.check_op_config():
            self.signin_first_time()

        self._token = None
        self._expiration = None

    @staticmethod
    def check_op_config():
        config_path = os.path.join(Path.home(), ".op", "config")

        try:
            open(config_path, 'r')
            return True
        except IOError:
            return False

    def write_token(self, token):
        file = open(self._token_path, "w")

        file.write(token + '\n')

        expiration = self.expiration()
        file.write(expiration + '\n')

        file.close()

    @staticmethod
    def expiration():
        expiration = datetime.now() + timedelta(minutes=30)
        return expiration.strftime("%Y-%m-%d %H:%M:%S.%f")

    def check_session_token(self):
        """Check if a session token already exists. If it does, check that it is not expired."""
        try:
            file = open(self._token_path, 'r')
            lines = file.readlines()

            self._token = lines[0].rstrip()
            self._expiration = datetime.strptime(lines[1].rstrip(), "%Y-%m-%d %H:%M:%S.%f")

            if self._expiration > datetime.now():
                return True
            else:
                print("Credentials expired !")
                return False
        except IOError:
            print("Temporary credentials do not exist, creating file ...")

        return False

    def signin(self):
        """Signin to the 1Password service and return the session token"""

        exists = self.check_session_token()

        if not exists:
            session_token = subprocess.check_output(
                ["op", "signin", "my", "--output=raw"],
                universal_newlines=True
            ).rstrip()

            self.write_token(session_token)

            self._token = session_token
            self._expiration = self.expiration()

        return True

    @staticmethod
    def signin_first_time():
        """Signin to the 1Password service for the first time"""

        print("Signin in with the 1Password op CLI for the first time, your password may be asked for twice !")


        email = input("Enter your 1Password email: ")
        key = input("Enter your 1Password master key: ")

        subprocess.check_output(
            ["op", "signin", "https://my.1password.com", email, key]
        )

    def get_token(self, service):
        """Get the MFA token for a service"""

        # `op` provides `op get totp <item>` but it does not match on the exact <item> name
        # contrary to `op get item <item>`
        item = subprocess.check_output(
            ["op", "get", "item", service, "--session={}".format(self._token)],
            universal_newlines=True
        ).rstrip()

        uuid = json.loads(item)['uuid']

        totp = subprocess.check_output(
            ["op", "get", "totp", uuid, "--session={}".format(self._token)],
            universal_newlines=True
        ).rstrip()

        return totp
