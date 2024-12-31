# custom_hashers.py
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.conf import settings
from django.utils.encoding import force_bytes

class CustomPBKDF2PasswordHasher(PBKDF2PasswordHasher):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def salt(self):
        # set to main app, main is main application
        return settings.APP_SECRET_KEYS.get('main')

    def encode(self, password, salt, iterations=None):
        """
        Melakukan hash password dengan menggunakan secret key yang ditentukan
        """
        return super().encode(password, self.salt(), iterations)

    def verify(self, password, encoded):
        """
        Memverifikasi password dengan menggunakan secret key yang ditentukan
        """
        return super().verify(password, encoded)
