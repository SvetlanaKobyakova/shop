from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('registration/', views.registration, name='registration'),
]
