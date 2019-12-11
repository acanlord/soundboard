from django.db import models
from django.contrib.auth.models import User

import hashlib

class AudioFile(models.Model):
    app_label = 'soundboard'

    absolute_path = models.CharField(max_length=255)

    filename = models.CharField(max_length=255)

    file = models.FileField(upload_to='custom_sounds/', null=True, blank=True)

def get_gravatar(self):
        # This is the example code found online for Gravatar, which will
        # randomly generate avatars based on email (we'll use user.username in
        # this case).
        email = self.user.username
        encoded = hashlib.md5(email.encode('utf8')).hexdigest()
        gravatar_url = "http://www.gravatar.com/avatar/%s?d=identicon" % encoded
        return gravatar_url