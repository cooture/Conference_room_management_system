from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.




class web:
    def test(requset):
        return HttpResponse("This is web test", status=202)

    def is_online(request):
        data = {
            'status': 200,
            'isrunning': True,
            'data': "Server is running"
        }
        return JsonResponse(data, safe=False)


class android:
    def test(request):
        return HttpResponse("this is android test", status=202)