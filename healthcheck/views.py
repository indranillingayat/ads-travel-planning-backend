from django.http import HttpResponse


def health_check(req):
    return HttpResponse("ok")
