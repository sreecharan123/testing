from django.urls import path
from .views import BookListCreate, BookRetrieveUpdateDestroy, AuthorListCreate
from . import views

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-retrieve-update-destroy'),
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('api/books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
]
