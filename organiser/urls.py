from django.urls import path
from .views import *



urlpatterns = [
    path('organiser_list/', OrganiserListView.as_view()),
    path('create_organiser/', OrganiserCreateView.as_view()),
    path('organiser_detail/<uuid:uid>/', OrganiserRetrieveView.as_view()),
    path('update_organiser/<uuid:uid>/', OrganiserUpdateView.as_view()),
    path('delete_organiser/<uuid:uid>/', OrganiserDeleteView.as_view()),

]
