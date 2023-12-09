from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='main_page'),
    path('books/', views.BookView.as_view(), name='books_page'),
    path('book-info/<slug:book_slug>/', views.BookInfo.as_view(), name='book_page'),
    path('authors/', views.AuthorView.as_view(), name='authors_page'),
    path('author-info/<slug:author_slug>/', views.AuthorInfo.as_view(), name='author_page'),
    path('add-author/', views.AddAuthor.as_view(), name='add_author_page'),
    path('add-book/', views.AddBook.as_view(), name='add_book_page'),
    path('update-book/<slug:book_slug>/', views.UpdateBook.as_view(), name='update_book_page'),
    path('delete-book/<slug:book_slug>/', views.DeleteBook.as_view(), name='delete_book_page'),
    path('update-author/<slug:author_slug>/', views.UpdateAuthor.as_view(), name='update_author_page'),
    path('delete-author/<slug:author_slug>/', views.DeleteAuthor.as_view(), name='delete_author_page'),
]
