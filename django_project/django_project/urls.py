"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from horoscope import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('aries/', views.aries),
    path('taurus/', views.taurus),
    path('gemini/', views.gemini),
    path('cancer/', views.cancer),
    path('leo/', views.leo),
    path('virgo/', views.virgo),
    path('libra/', views.libra),
    path('scorpio/', views.scorpio),
    path('sagittarius/', views.sagittarius),
    path('capricorn/', views.capricorn),
    path('aquarius/', views.aquarius),
    path('pisces/', views.pisces)
]
