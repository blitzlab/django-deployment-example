from django.urls import path
from . import views

app_name ='basic_app'

urlpatterns = [
    path('other', views.other, name = 'other'),
    path('relative', views.relative, name = 'relative')
]
