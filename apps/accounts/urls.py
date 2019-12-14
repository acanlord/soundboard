from django.urls import path

from apps.accounts import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin

# In this example, we've separated out the views.py into a new file
urlpatterns = [
    #path('', views.index, name = 'index'),
    #path('', views.index, name = 'home'),
    #path('upload', views.upload, name = 'upload'),
    #path('admin', views.upload),
    path('login/', views.log_in, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('users/', views.view_all_users, name='view_all_users'),
    path('users/<username>/', views.view_profile, name='view_profile'),
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static

# Changed to include files in the media folder
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)