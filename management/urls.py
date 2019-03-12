from django.urls import path, include
from management import views
from .api_transfer import api

urlpatterns = [
    path('', include(api))
]