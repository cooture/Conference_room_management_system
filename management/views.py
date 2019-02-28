from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    data = {'hell': 111}
    return HttpResponse("hello world")


def test(request):
    return HttpResponse(content="hello world", status=202)


class apis:
    def is_online(request):
        data = {
            'status': 200,
            'data': "Server is running"
        }
        return JsonResponse(1234, safe=False)
