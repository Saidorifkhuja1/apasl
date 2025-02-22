from django.urls import path
from .views import *

urlpatterns = [
    path('books_list/', BookListView.as_view()),
    path('create_book/', BookCreateView.as_view()),
    path('book_detail/<uuid:uid>/', BookRetrieveView.as_view()),
    path('update_book/<uuid:uid>/', BookUpdateView.as_view()),
    path('delete_book/<uuid:uid>/', BookDeleteView.as_view()),
    path('books_list_russian/', BookListRussianView.as_view()),
    path('book_detail_russian/<uuid:uid>/', BookRetrieveRussianView.as_view()),
    path('books_list_english/', BookListEnglishView.as_view()),
    path('book_detail_english/<uuid:uid>//', BookRetrieveEnglishView.as_view()),
]



