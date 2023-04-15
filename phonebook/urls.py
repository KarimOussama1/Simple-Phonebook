from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'phonebook'

urlpatterns = [
    path('', views.show_contacts, name='show_contacts'),
    path('contact_detail/<int:id>', views.contact_detail, name='contact_detail'),
    path('new_contact', views.new_contact, name='new_contact'),
    path('add_contact', views.add_contact, name='add_contact'),
]

urlpatterns += staticfiles_urlpatterns()