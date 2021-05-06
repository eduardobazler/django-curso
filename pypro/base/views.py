from django.shortcuts import render # noqa
from django.http.response import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('Olá Django, Eduardo Bazler!')
