from django.urls import path
from .views import *

urlpatterns = [
    path('/',view=number_view)
]