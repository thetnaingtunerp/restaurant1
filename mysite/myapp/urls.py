from django.urls import path
from .views import *
from . import views
app_name = 'myapp'
urlpatterns = [
    path('',views.test, name='test'),
    path('itemlist/', itemlist.as_view(), name= 'itemlist'),
    ]