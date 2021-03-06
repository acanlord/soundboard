from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from newsounds import views
from django.conf.urls import url, include
from django.contrib import admin

# In this example, we've separated out the views.py into a new file
urlpatterns = [
    path('', views.index, name = 'index'),
    path('', views.index, name = 'home'),
    path('upload', views.upload, name = 'upload'),
    path('admin', views.upload),
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static

# Changed to include files in the media folder
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)