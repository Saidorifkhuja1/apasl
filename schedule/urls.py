from django.urls import path
from .views import *



urlpatterns = [
    path('schedules_list/', ScheduleListView.as_view()),
    path('create_schedule/', ScheduleCreateView.as_view()),
    path('schedule_detail/<uuid:uid>/', ScheduleRetrieveView.as_view()),
    path('update_schedule/<uuid:uid>/', ScheduleUpdateView.as_view()),
    path('delete_schedule/<uuid:uid>/', ScheduleDeleteView.as_view()),
    path('schedules_list_ru/', ScheduleListRussianView.as_view()),
    path('schedules_detail_ru/<uuid:uid>/', ScheduleRetrieveRussianView.as_view()),
    path('schedules_list_en/', ScheduleListEnglishView.as_view()),
    path('schedules_detail_en/<uuid:uid>/', ScheduleRetrieveEnglishView.as_view()),

]






