from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.accounts.forms import UserEditForm, SignupForm
from apps.accounts.models import User
#from .models import AudioFile

# def index(request):

#     all_audio_files = AudioFile.objects.all()

#     if request.user.is_authenticated:
#         all_audio_files = AudioFile.objects.filter(user=request.user)

#     print('tessadflasfdjlkasfdjlksadfjlasfdjlkjlkasdfjkladsfljkasdfljkasdfjlkasdfkljt')
#     context = {

#         'audio_files' : all_audio_files,
#     }
#     return render(request, 'index.html', context)

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'pages/login.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Log-in the user right away
            messages.success(request, 'Account created successfully. Welcome!')
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'pages/signup.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out.')
    return redirect('/')


def view_all_users(request):
    all_users = User.objects.all()
    context = {
        'users': all_users,
    }
    return render(request, 'accounts/view_all_users.html', context)


def view_profile(request, username):
    user = User.objects.get(username=username)

    if request.user == user:
        is_viewing_self = True
    else:
        is_viewing_self = False

    context = {
        'user': user,
        'is_viewing_self': is_viewing_self,
    }
    return render(request, 'accounts/profile_page.html', context)

# def upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         fn = fs.save(myfile.name, myfile)
#         upload_file_url = fs.url(fn)
        

#         # Make the database entry
#         post = AudioFile.objects.create(
#            absolute_path = os.path.join(settings.MEDIA_URL, fn),
#            filename = fn,
#            user=request.user,
#         )

#         return render(request, 'upload.html', {
#             'uploaded_file_url': upload_file_url 
#         })
#         return redirect('/')
#     return render(request, 'accounts/upload.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserEditForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'accounts/edit_profile.html', context)



