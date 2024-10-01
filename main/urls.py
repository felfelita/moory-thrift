from django.urls import path
from main.views import show_main, create_thrift_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_thrift, delete_thrift, contact_us




app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-thrift-entry', create_thrift_entry, name='create_thrift_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-thrift/<uuid:id>', edit_thrift, name='edit_thrift'),
    path('delete/<uuid:id>', delete_thrift, name='delete_thrift'), 
    path('contact/', contact_us, name='contact_us'),
]