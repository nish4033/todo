from django.contrib.auth.hashers import PBKDF2PasswordHasher


class CustomPBKDF2PasswordHasher(PBKDF2PasswordHasher):
    def encode(self, password, salt, iterations=None):
        encoded = super().encode(password, salt, iterations)
        return encoded[:50]
