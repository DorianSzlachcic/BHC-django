from django.urls import path
from api import views

urlpatterns = [
    path('generate_token/<username>/<channel>/', views.generate_token, name='generate_token'),
    path('place_in_queue/<username>/<channel>/', views.place_in_queue, name='place_in_queue'),
    path('brew_coffee/', views.brew_coffee, name='brew_coffee')
]
