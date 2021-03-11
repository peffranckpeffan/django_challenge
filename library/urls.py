from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.getAllBooks, name='books'),
    path('client/<str:pk_client>/books/', views.getLoanedBooks, name='loaned-books'),
    path('book/<str:pk_book>/reserve/client/<str:pk_client>/', views.makeBookReservation, name='reserve-book'),
]