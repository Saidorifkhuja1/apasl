from aiohttp.web_response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import *



class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]


class BookRetrieveView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'uid'
    # permission_classes = [IsAdminUser]



class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookUpdateSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsAdminUser]

#######################################################################
class BookListRussianView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookRussianSerializer




class BookRetrieveRussianView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookRussianSerializer
    lookup_field = 'uid'



class BookListEnglishView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookEnglishSerializer


class BookRetrieveEnglishView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookEnglishSerializer
    lookup_field = 'uid'

