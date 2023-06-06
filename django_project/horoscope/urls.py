from django.urls import path
from . import views as hv

urlpatterns = [
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
    path('pisces/', hv.pisces)
]