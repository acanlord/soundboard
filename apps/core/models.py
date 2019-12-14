from django.db import models
from apps.accounts.models import User

# Create your models here.
class AudioFile(models.Model):
    app_label = 'soundboard'
    absolute_path = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
