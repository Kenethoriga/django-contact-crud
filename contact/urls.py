from django.urls import path 
from . import views 
from . views import (
    ContactCreateView,
    contact_update,
    ContactDeleteView,
    ContactListView,
    ContactDetailView,
)
urlpatterns = [
    path('',ContactListView.as_view(),name="contact-list"),
    path('search',views.search,name="search"),
    path('create',ContactCreateView.as_view(),name="contact-create"),
    path('contact_detail/<int:pk>/',ContactDetailView.as_view(),name="contact-detail"),
    path('update/<int:pk>/',views.contact_update, name="contact-update"),
    path('delete/<int:pk>/',ContactDeleteView.as_view(), name="contact-delete"),
]




