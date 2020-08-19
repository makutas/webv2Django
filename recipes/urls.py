from django.urls import path
from . import views

app_name = 'recipes'
urlpatterns = [
    # HOME PAGE
    path('', views.index, name='index')
]