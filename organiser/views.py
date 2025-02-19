from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser

class OrganiserCreateView(generics.CreateAPIView):
    queryset = Organiser.objects.all()
    serializer_class = OrganiserSerializer
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]


class OrganiserRetrieveView(generics.RetrieveAPIView):
    queryset = Organiser.objects.all()
    serializer_class = OrganiserSerializer
    lookup_field = 'uid'
    # permission_classes = [IsAdminUser]


class OrganiserUpdateView(generics.UpdateAPIView):
    queryset = Organiser.objects.all()
    serializer_class = OrganiserSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]


class OrganiserDeleteView(generics.DestroyAPIView):
    queryset = Organiser.objects.all()
    serializer_class = OrganiserSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]


class OrganiserListView(generics.ListAPIView):
    queryset = Organiser.objects.all()
    serializer_class = OrganiserSerializer
    # permission_classes = [IsAdminUser]
