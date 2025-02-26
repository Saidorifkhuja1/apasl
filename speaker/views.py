from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser

class SpeakerCreateView(generics.CreateAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]


class SpeakerRetrieveView(generics.RetrieveAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    lookup_field = 'uid'
    # permission_classes = [IsAdminUser]


class SpeakerUpdateView(generics.UpdateAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]


class SpeakerDeleteView(generics.DestroyAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]


class SpeakerListView(generics.ListAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    # permission_classes = [IsAdminUser]

##########################################################################

class SpeakerListRussianView(generics.ListAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerRussianSerializer

class SpeakerRetrieveRussianView(generics.RetrieveAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerRussianSerializer
    lookup_field = 'uid'

class SpeakerListEnglishView(generics.ListAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerEnglishSerializer

class SpeakerRetrieveEnglishView(generics.RetrieveAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerEnglishSerializer
    lookup_field = 'uid'

class SpeakerListUzbekView(generics.ListAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerUzbekSerializer

class SpeakerRetrieveUzbekView(generics.RetrieveAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerUzbekSerializer
    lookup_field = 'uid'





# class SpeakerListRussianView(generics.ListAPIView):
#     queryset = Speaker.objects.all()
#     serializer_class = SpeakerRussianSerializer
#
# class SpeakerRetrieveRussianView(generics.RetrieveAPIView):
#     queryset = Speaker.objects.all()
#     serializer_class = SpeakerRussianSerializer
#     lookup_field = 'uid'
#
#
# class SpeakerListEnglishView(generics.ListAPIView):
#     queryset = Speaker.objects.all()
#     serializer_class = SpeakerEnglishSerializer
#
#
# class SpeakerRetrieveEnglishView(generics.RetrieveAPIView):
#     queryset = Speaker.objects.all()
#     serializer_class = SpeakerEnglishSerializer
#     lookup_field = 'uid'
#
#
#
# class SpeakerListUzbekView(generics.ListAPIView):
#     queryset = Speaker.objects.all()
#     serializer_class = SpeakerUzbekSerializer
#
#
# class SpeakerRetrieveUzbekView(generics.RetrieveAPIView):
#     queryset = Speaker.objects.all()
#     serializer_class = SpeakerUzbekSerializer
#     lookup_field = 'uid'
