from django.urls import path
from week_days import views as wdv
urlpatterns = [
    path('monday/', wdv.monday),
    path('tuesday/', wdv.tuesday)
]