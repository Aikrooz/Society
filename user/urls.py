from django.urls import path
from .views import RegisterView,login

urlpatterns = [
    path('login/', login, name='login'),
    path('register/',RegisterView.as_view(),name='register')
]