from django.urls import path

from apps.core import views

urlpatterns = [
	path('', views.index, name = 'index'),
    path('', views.index, name = 'home'),
    path('upload', views.upload, name = 'upload'),
    path('admin', views.upload),
]

