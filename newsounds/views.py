import requests
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
# from django.contrib.auth.models import User

# Import db model
from .models import AudioFile

# Uploads
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage

#Test what we think current root is
#curr_path = os.path.dirname(os.path.abspath(__file__))
# curr_path = os.path.join(settings.MEDIA_ROOT),
# print ("Your current path is", curr_path)

def index(request):

    all_audio_files = AudioFile.objects.all()
    context = {
        'audio_files' : all_audio_files,
    }
    return render(request, 'index.html', context)


def sound(request):
    context = {}
    return render(request, 'sound.html', context) 

def uploads(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fn = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)

        # Make the database entry
        post = AudioFile.objects.create(
            absolute_path = os.path.join(settings.MEDIA_ROOT, fn),
            filename = fn
        )

        return render(request, 'uploads.html', {
            'uploaded_file_url': fn
        })
    return render(request, 'uploads.html')