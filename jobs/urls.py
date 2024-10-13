from django.urls import path
from jobs import views

urlpatterns = [
    path('', views.jobOffers, name='jobs_list'),
    path('your_offers/', views.yourOffers, name='your_offers'),
    path('add/', views.add, name='addOffer'),
    path('<id>/', views.jobDetails, name='details'),
    path('edit/<id>/', views.edit, name='editOffer'),
    path('delete/<id>/', views.delete, name='delete'),
    path('apply/<id>/', views.apply, name='apply'),
    path('open_room/<id>/', views.open_room, name='openRoom'),
]
