
from unicodedata import name
from django.contrib import admin
from django.urls import path
from . views  import *

urlpatterns = [
  
    path('filehandle/', HandleFilesURL.as_view()),
    path('', index , name= 'home')
]
