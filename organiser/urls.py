from django.urls import path
from .views import *



urlpatterns = [
    path('organiser_list/', OrganiserListView.as_view()),
    path('create_organiser/', OrganiserCreateView.as_view()),
    path('organiser_detail/<uuid:uid>/', OrganiserRetrieveView.as_view()),
    path('update_organiser/<uuid:uid>/', OrganiserUpdateView.as_view()),
    path('delete_organiser/<uuid:uid>/', OrganiserDeleteView.as_view()),
    path('organisers_list_russian/', OrganiserListRussianView.as_view()),
    path('organiser_detail_russian/<uuid:uid>/', OrganiserRetrieveRussianView.as_view()),
    path('organisers_list_english/', OrganiserListEnglishView.as_view()),
    path('organisers_detail_english/<uuid:uid>/', OrganiserRetrieveEnglishView.as_view()),

]
