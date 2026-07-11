from django.urls import path
from . import views
from .views import *

urlpatterns = [
   path('students/', StudentApiView.as_view(), name='student-create'),
]