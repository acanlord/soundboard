from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from newsounds import views

# In this example, we've separated out the views.py into a new file
urlpatterns = [
    path('', views.index),
    path('sound', views.sound),
    path('uploads', views.uploads),
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Changed to include files in the media folder
urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)