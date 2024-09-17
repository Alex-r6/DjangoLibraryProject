from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('author/list/', views.author_list, name='author-list'),
    path('book/list/', views.book_list, name='book-list'),
    path('author/detail/<slug:slug>/', views.author_detail, name='author-detail'),
    path('genre/list/', views.genre_list, name='genre-list'),
    path('book/detail/<int:pk>/', views.book_detail, name='book-detail'),
    path('add/new/comment/v1/', views.add_new_comment1, name='add-new-comment-1'),
    path('add/new/comment/v2/<int:pk>/', views.add_new_comment2, name='add-new-comment-2'),
    path('api/author/list/', views.AuthorListAPIView.as_view()),
    path('api/author/<int:pk>/', views.AuthorRetrieveAPIView.as_view()),
    path('api/book/list/', views.BookListAPIView.as_view()),
    path('api/book/<int:pk>/', views.BookRetrieveAPIView.as_view()),
    path('api/genre/list/', views.GenreListAPIView.as_view()),
    path('api/genre/<int:pk>/', views.GenreRetrieveAPIView.as_view()),
    path('api/comment/list/', views.CommentListAPIView.as_view()),
    path('api/comment/<int:pk>/', views.CommentRetrieveAPIView.as_view()),
    path('api/book/update/<int:pk>/', views.BookRetrieveUpdateAPIView.as_view()),
    path('user/sign/out/', views.user_sign_out, name='user-sign-out'),
    path('user/sign/in/', views.user_sign_in, name='user-sign-in'),
    path('change/favor/book/<int:pk>/', views.change_favorite_status, name='change-favorite-status'),
    path('search/', views.search, name='search'),
    path('add/new/author/', views.add_new_author, name='add-new-author'),
    path('add/new/book/', views.add_new_book, name='add-new-book'),
    path('user/creation/', views.user_creation_template, name='user-creation-template'),
    path('add/new/user/', views.add_new_user, name='add-new-user')

]
