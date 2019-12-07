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
curr_path = os.path.join(settings.MEDIA_URL),
print ("Your current path is", curr_path)




def custom(request):

    all_audio_files = AudioFile.objects.all()
    context = {
        'audio_files' : all_audio_files,
    }
    return render(request, 'custom.html', context)

def index(request):

    #all_audio_files = AudioFile.objects.all()
    context = {
        #'audio_files' : all_audio_files,
    }
    return render(request, 'index.html', context)

#def index(request):
    

    # for File in AudioFile.objects.all():
    # # You can do the below even better if you use the same method as the model uses
    # # to generate upload_to
    #     file_name = 'my_file_this_should_depend_on_myModel'
    #     file_location = '/media%s' % file_name
    #     print "UPDATE app_mymodel SET file_field='%s' WHERE id=%s;" % \ 
    #         (file_location, AudioFile.id)


    #all_audio_files = AudioFile.objects.all()
            # context = {
            # 'audio_files' : filename,
            # }
            # return render(request, 'index.html', context)


def uploads(request):
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

        return render(request, 'uploads.html', {
            'uploaded_file_url': upload_file_url 
        })
    return render(request, 'uploads.html')