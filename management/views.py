from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.


class general:
    def test(request):
        return HttpResponse("This is gen test", status=202)


class web:
    def test(requset):
        return HttpResponse("This is web test", status=202)

    def is_online(request):
        data = {
            'status': 202,
            'isrunning': True,
            'data': "Server is running"
        }
        return JsonResponse(data, safe=False)

    def static_test(request):
        return render(request, 'web/index.html')


class android:
    def test(request):
        return HttpResponse("this is android test", status=202)