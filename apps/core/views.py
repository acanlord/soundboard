import requests
import os
from django.conf import settings
from .models import AudioFile
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.accounts.forms import UserEditForm, SignupForm
from apps.accounts.models import User
# Two example views. Change or delete as necessary.


def index(request):

    all_audio_files = AudioFile.objects.all()

    if request.user.is_authenticated:
        all_audio_files = AudioFile.objects.filter(user=request.user)

    print('tessadflasfdjlkasfdjlksadfjlasfdjlkjlkasdfjkladsfljkasdfljkasdfjlkasdfkljt')
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
           filename = fn,
           user=request.user,
        )

        return render(request, 'upload.html', {
            'uploaded_file_url': upload_file_url 
        })
    return render(request, 'accounts/upload.html')