from django.shortcuts import render # noqa
from django.http.response import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('<html><body>Olá Django, Eduardo Bazler!</body></html>', content_type='text/html')
