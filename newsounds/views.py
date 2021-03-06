import requests
import os
from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import AudioFile


def index(request):

    all_audio_files = AudioFile.objects.all()
    context = {
        'audio_files' : all_audio_files,
    }
    return render(request, 'index.html', context)

def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fn = fs.save(myfile.name, myfile)
        upload_file_url = fs.url(fn)
        

        # Make the database entry
        post = AudioFile.objects.create(
           absolute_path = os.path.join(settings.MEDIA_URL, fn),
           filename = fn
        )

        return render(request, 'upload.html', {
            'uploaded_file_url': upload_file_url 
        })
    return render(request, 'upload.html')
