from django.urls import path
from .views import *



urlpatterns = [
    path('speakers_list/', SpeakerListView.as_view()),
    path('create_speaker/', SpeakerCreateView.as_view()),
    path('speaker_detail/<uuid:uid>/', SpeakerRetrieveView.as_view()),
    path('update_speaker/<uuid:uid>/', SpeakerUpdateView.as_view()),
    path('delete_speaker/<uuid:uid>/', SpeakerDeleteView.as_view()),
    path('speakers_list_ru/', SpeakerListRussianView.as_view()),
    path('speakers_details_ru/<uuid:uid>/', SpeakerRetrieveRussianView.as_view()),
    path('speaker_list_en/', SpeakerListEnglishView.as_view()),
    path('speakers_details_en/<uuid:uid>/', SpeakerRetrieveEnglishView.as_view()),
    path('speaker_list_uz/', SpeakerListUzbekView.as_view()),
    path('speakers_details_uz/<uuid:uid>/', SpeakerRetrieveUzbekView.as_view()),

]


