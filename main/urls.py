from django.urls import path
from main.views import show_main, create_thrift_entry


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-mood-entry', create_thrift_entry, name='create_thrift_entry'),

]