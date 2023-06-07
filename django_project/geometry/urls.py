from django.urls import path
from geometry import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', views.get_square_rec, name='rectangle'),
    path('square/<int:width>/', views.get_square_sq, name='square'),
    path('circle/<int:radius>/', views.get_square_cr, name='circle'),
    path('rectangle_area/<int:width>/<int:height>/', views.get_square_rec_area),
    path('square_area/<int:width>/', views.get_square_sq_area),
    path('circle_area/<int:radius>/', views.get_square_cr_area)
]
