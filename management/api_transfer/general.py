from django.urls import path
from management.views import general

urlpatterns = [
    path('test/', general.test),
    path('getallusers/', general.getAllUsers),
    path('getsomeone/', general.getSomeone),
    path('searchsomebody/', general.searchSomebody),
    path('updateuser/', general.updateSomeone),
    path('getusermeeting/', general.getUserMeeting)

]
