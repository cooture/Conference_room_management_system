from django.urls import path, include
from management.views import android


urlpatterns = [
    path('test/', android.test)
]