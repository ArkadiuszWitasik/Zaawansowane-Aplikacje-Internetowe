"""
URL configuration for music project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from musicApp.views import all, details, addAlbum, updateAlbum, deleteAlbum


urlpatterns = [
    path('all/', all),
    path('details/<int:album_id>/', details),
    path('add-album/', addAlbum),
    path('update-album/<int:album_id>/', updateAlbum),
    path('delete-album/<int:album_id>/', deleteAlbum)
]
