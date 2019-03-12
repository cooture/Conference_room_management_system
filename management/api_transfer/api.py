from django.urls import path, include
from . import web,android

urlpatterns = [
    path('web/', include(web)),
    path('android/', include(android))

]