from django.urls import path, include
import management.urls
urlpatterns =[
    path("apis/v1.0/", include(management.urls))
]