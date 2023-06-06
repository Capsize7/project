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
from horoscope import views as hv
from week_days import views as wdv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aries/', hv.aries),
    path('taurus/', hv.taurus),
    path('gemini/', hv.gemini),
    path('cancer/', hv.cancer),
    path('leo/', hv.leo),
    path('virgo/', hv.virgo),
    path('libra/', hv.libra),
    path('scorpio/', hv.scorpio),
    path('sagittarius/', hv.sagittarius),
    path('capricorn/', hv.capricorn),
    path('aquarius/', hv.aquarius),
    path('pisces/', hv.pisces),
    path('todo_week/monday/', wdv.monday),
    path('todo_week/tuesday/', wdv.tuesday)
]
