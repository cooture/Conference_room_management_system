from django.urls import path
from management import views
from management.views import apis

urlpatterns = [
    path('isonline/', apis.is_online)
]