from django.urls import path
from .views import *

urlpatterns = [
    path('books_list/', BookListView.as_view()),
    path('create_book/', BookCreateView.as_view()),
    path('book_detail/<uuid:uid>/', BookRetrieveView.as_view()),
    path('update_book/<uuid:uid>/', BookUpdateView.as_view()),
    path('delete_book/<uuid:uid>/', BookDeleteView.as_view()),
    path('books_list_ru/', BookListRussianView.as_view()),
    path('book_detail_ru/<uuid:uid>/', BookRetrieveRussianView.as_view()),
    path('books_list_en/', BookListEnglishView.as_view()),
    path('book_detail_en/<uuid:uid>/', BookRetrieveEnglishView.as_view()),
]



