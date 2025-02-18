from django.urls import path
from .views import *



urlpatterns = [
    path('speakers_list/', SpeakerListView.as_view()),
    path('create_speaker/', SpeakerCreateView.as_view()),
    path('speaker_detail/<uuid:uid>/', SpeakerRetrieveView.as_view()),
    path('update_speaker/<uuid:uid>/', SpeakerUpdateView.as_view()),
    path('delete_speaker/<uuid:uid>/', SpeakerDeleteView.as_view()),

]


