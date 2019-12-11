from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from newsounds import views
from django.conf.urls import url, include
from django.contrib import admin

# In this example, we've separated out the views.py into a new file
urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload'),
    path('admin/', admin.site.urls),
    path('sign_up/', views.sign_up),
    path('log_in/custom/', views.custom, name='custom'),
	path('log_in/', views.log_in, name='log_in'),
	path('logout/', views.logout_view, name='logout'),
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Changed to include files in the media folder
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
