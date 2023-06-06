from django.urls import path
from week_days import views as wdv
urlpatterns = [
    path('todo_week/monday/', wdv.monday),
    path('todo_week/tuesday/', wdv.tuesday)
]