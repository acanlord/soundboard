import requests
import os
from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth.models import User

# Import db model
from .models import AudioFile

# Uploads
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# def index(request):
#     post = AudioFile.objects.create(
#         #absolute_path="/some/path/to/a/file.wav",
#         absolute_path="{ path_to_file }",
#         filename="{ file_name }"
#     )

def index(request):
    post = AudioFile.objects.create(
        save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', request.FILES['file'])
        path = default_storage.save(save_path, request.FILES['file'])
        #return default_storage.path(path)
    )


     all_audio_files = AudioFile.objects.all()
    context = {
        'audio_files' : all_audio_files
    }
    return render(request, 'templates/index.html', context)


def sound(request):
    context = {}
    return render(request, 'sound.html', context) 

def uploads(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'uploads.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'uploads.html')
