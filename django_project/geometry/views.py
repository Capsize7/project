from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from math import pi
from django.urls import reverse

# Create your views here.

def get_square_rec(request, width, height):
    return HttpResponse(f"Площадь прямоугольника размером {width}x{height} равна {width * height}")

def get_square_rec_area(request, width, height):
    redirect_url = reverse('rectangle', args=(width, height))
    return HttpResponseRedirect(redirect_url)

def get_square_sq(request, width):
    return HttpResponse(f"Площадь квадрата размером {width}х{width} равна {width * width}")

def get_square_sq_area(request, width):
    redirect_url = reverse('square', args=(width,))
    return HttpResponseRedirect(redirect_url)


def get_square_cr(request, radius):
    return HttpResponse(f"Площадь круга радиуса {radius} равна {round(pi * radius ** 2, 1)}")


def get_square_cr_area(request, radius):
    redirect_url = reverse('circle', args=(radius,))
    return HttpResponseRedirect(redirect_url)
