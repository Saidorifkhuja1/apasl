from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser

class ScheduleCreateView(generics.CreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAdminUser]



class ScheduleRetrieveView(generics.RetrieveAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    lookup_field = 'uid'
    # permission_classes = [IsAdminUser]


class ScheduleUpdateView(generics.UpdateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]



class ScheduleDeleteView(generics.DestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]


class ScheduleListView(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    # permission_classes = [IsAdminUser]

###################################################################

class ScheduleListRussianView(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleRussianSerializer

class ScheduleRetrieveRussianView(generics.RetrieveAPIView):
        queryset = Schedule.objects.all()
        serializer_class = ScheduleRussianSerializer
        lookup_field = 'uid'



class ScheduleListEnglishView(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleEnglishSerializer



class ScheduleRetrieveEnglishView(generics.RetrieveAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleEnglishSerializer
    lookup_field = 'uid'




