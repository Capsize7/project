from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def leo(request):
    return HttpResponse("Знак зодиака - Лев")

def scorpio(request):
    return HttpResponse("Знак зодиака - Скорпион")


def aries(request):
    return HttpResponse("Знак зодиака - Овен")

def capricorn(request):
    return HttpResponse("Знак зодиака - Козерог")
