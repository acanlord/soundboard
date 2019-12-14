import hashlib

from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User class which extends built-in User. Presently, just adds a "bio"
# and a gravatar method. Feel free to add your own new fields here!

class User(AbstractUser):

    bio = models.TextField()

    def gravatar(self, size=None):
        GRAVATAR_URL = 'https://gravatar.com/avatar/%s?d=identicon%s'
        email = str(self.email).strip().lower()
        digest = hashlib.md5(email.encode('utf-8')).hexdigest()

        if size:
            size_str = '&s=%i' % size
        else:
            size_str = ''

        return GRAVATAR_URL % (digest, size_str)

# class AudioFile(models.Model):
#     #app_label = 'soundboard'
#     # DONT USE THISSSS ITS NOT REAL
#     absolute_path = models.CharField(max_length=255)
#     filename = models.CharField(max_length=255)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

