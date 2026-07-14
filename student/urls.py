from django.urls import path
from . import views
from .views import *

urlpatterns = [
   path('', StudentApiView.as_view(), name='student-create'),
   path('<int:id>/', StudentApiView.as_view(), name='student-detail'),
]