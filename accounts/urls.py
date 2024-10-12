from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage ,name='home'),
    path('login/',views.loginPage ,name='login'),
    path('logout/',views.logoutUser ,name='logout'),
    path('register/',views.registerPage ,name='register'),
    path('registerCompany/',views.registerCompany, name='registerCompany')
]