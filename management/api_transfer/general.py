from django.urls import path
from management.views import general

urlpatterns = [
    path('test/', general.test)
]
