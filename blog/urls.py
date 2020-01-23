from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Blog Home"),
    path('about/', views.about, name="About"),
    path('contact/', views.contact, name="Contact"),
    path('login/', views.login, name="Login"),
    path('register/', views.contact, name="Register"),
    path('menu/', views.contact, name="Menu"),
    path('single/', views.single, name="Single"),
]