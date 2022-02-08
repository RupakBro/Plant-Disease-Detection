from django.urls import path
from . import views # 1
from .views.views import index ,login
urlpatterns = [
    path('home', index, name='homepage'),
    path('', login , name='loginpage'),
]