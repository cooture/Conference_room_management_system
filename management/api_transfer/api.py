from django.urls import path, include
from . import web, android, general

urlpatterns = [
    path('web/', include(web)),
    path('android/', include(android)),
    path('gen/', include(general))

]
