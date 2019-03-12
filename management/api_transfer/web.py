from django.urls import path, include
from management.views import web

urlpatterns = [
    path('test/', web.test),
    path('isonline/', web.is_online)
]
