from django.urls import path
from horoscope import views
urlpatterns = [
    path('', views.index),
    path('types/', views.get_types),
    path('types/<att>', views.get_types_att, name='att-name'),
    path('<int:day>/<int:month>/', views.get_zodiac_date),
    path('<int:zodiac>/', views.get_zodiac_by_number),
    path('<str:zodiac>/', views.get_zodiac_by_name, name='horoscope-name'),

]
