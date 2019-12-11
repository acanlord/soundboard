import requests
import os
from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm
from django.utils.datastructures import MultiValueDictKeyError
# from django.contrib.auth.models import User

# Import db model
from .models import AudioFile

# Uploads
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage

# Users
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from django.contrib import auth

#login
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#from apps.accounts.forms import UserEditForm, SignupForm
#from apps.accounts.models import User

#Test what we think current root is
#curr_path = os.path.dirname(os.path.abspath(__file__))
curr_path = os.path.join(settings.MEDIA_URL),
print ("Your current path is", curr_path)



class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']



class AudioFileForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = ['file', 'filename']

def index(request):

    all_audio_files = AudioFile.objects.all()
    
    context = {

        'audio_files' : all_audio_files,
    }
    return render(request, 'index.html', context)

def sign_up(request):
    

    if request.method == 'POST':

        form = NewUserForm(request.POST)

        if form.is_valid():            
            user = form.save()
            auth.login(request, user)

            return redirect('/')

    else:        
        form = NewUserForm()

    users = User.objects.all()    

    context = {
        'form': form,
    }
    return render(request, 'sign_up.html', context)

# def custom(request):

#     all_audio_files = AudioFile.objects.all()
#     context = {
#         'audio_files' : all_audio_files,
#     }
#     return render(request, 'custom.html', context)

def log_in(request):

    users = User.objects.all()
    
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            #auth.login(request, user)
            auth.login(request, form.get_user())
            return redirect('custom')
    else:
        form = AuthenticationForm()



    context = {
        'form': form,
    }
    return render(request, 'registration/log_in.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out.')
    return redirect('/')


def custom(request, username):

    user = User.objects.get(username=username)

    if request.user == user:
        is_viewing_self = True
    else:
        is_viewing_self = False


    all_audio_files = AudioFile.objects.all()
    # CREATE tweets
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request,
        # including uploaded files
        form = AudioFile(request.POST, request.FILES)

        if form.is_valid():
            # Use the form to save
            audio_file = form.save(commit=False)
            audio_file.user = request.user
            audio_file.save()
            # Cool trick to redirect to the previous page
            return redirect(request.META.get('HTTP_REFERER', '/'))

    else:
        # if a GET we'll create a blank form
        form = AudioFile()

    # READ tweets and User information from database
    # We can break down complicated filtering of "querysets" into multiple
    # lines like this
    audio_files = AudioFile.objects.order_by('-created')
    audio_files_by_user = audio_files.filter(user=user)

    context = {
        'is is_viewing_self': is_viewing_self,
        'audio_files': audio_files_by_user,
        'form': form,
        'user_on_page': user,
        'is_me': user == request.user,

    }
    return render(request, 'custom.html', context)



def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fn = fs.save(myfile.name, myfile)
        upload_file_url = fs.url(fn)
        

        # Make the database entry
        post = AudioFile.objects.create(
            #Django does not care about absolute path. 
           #absolute_path = os.path.join(settings.MEDIA_ROOT, fn),
           absolute_path = os.path.join(settings.MEDIA_URL, fn),
           filename = fn
        )

        return render(request, 'upload.html', {
            'uploaded_file_url': upload_file_url 
        })
    return render(request, 'upload.html')

def edit_user_profile(request, username):
    # Get the user we are looking for
    user = User.objects.get(username=username)

    if request.method == 'POST':

        # Create a form instance and populate it with data from the request
        form = EditUserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('/users/' + user.username)

    else:
        # A GET, create a pre-filled form with the instance.
        form = EditUserForm(instance=user)

    context = {
        'form': form,
    }
    return render(request, 'edit_user_profile.html', context)