from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Count, Q
from rest_framework import generics

from .models import *
from .forms import *
from .serializers import *


def index(request):
    user = request.user
    if user.is_authenticated:
        context = {
            'authors_num': Author.objects.count(),
            'books_num': Book.objects.count(),
            'genres_num': Genre.objects.count(),
            'favor_list': user.profile.favorite_books.all()
        }
    else:
        context = {
            'authors_num': Author.objects.count(),
            'books_num': Book.objects.count(),
            'genres_num': Genre.objects.count(),
        }
    return render(
        request,
        template_name='library/index.html',
        context=context
    )


def author_list(request):
    context = {
        'author_list': Author.objects.all(),
        'form': AuthorForm()
    }
    return render(
        request,
        template_name='library/author_list.html',
        context=context
    )


def book_list(request):
    context = {
        'book_list': Book.objects.select_related('author').annotate(num_comments=Count('comments')).all(),
        'form': BookForm()
    }
    return render(
        request,
        template_name='library/book_list.html',
        context=context
    )


def author_detail(request, slug):
    context = {
        'author_detail': Author.objects.get(slug=slug)
    }
    return render(
        request,
        template_name='library/author_detail.html',
        context=context
    )


def genre_list(request):
    context = {
        'genre_list': Genre.objects.prefetch_related("books").all()
    }
    return render(
        request,
        template_name='library/genre_list.html',
        context=context
    )


def book_detail(request, pk):
    context = {
        'book_detail': Book.objects.get(id=pk),
        'comment_form': CommentForm(),
        # 'book_shop': BookShop.objects.get(id=pk)
    }
    return render(
        request,
        template_name='library/book_detail.html',
        context=context
    )


def add_new_comment1(request):
    username = request.POST.get('username')
    text = request.POST.get('text')
    book_id = request.POST.get('book_id')
    print(request.POST)
    if username and text:
        Comment.objects.create(username=username, text=text, book_id=book_id)
    return HttpResponseRedirect(reverse('library:book-detail', kwargs={'pk': book_id}))


def add_new_comment2(request, pk):
    f = CommentForm(request.POST)
    new_comment = f.save(commit=False)
    new_comment.book_id = pk
    new_comment.save()
    return HttpResponseRedirect(reverse('library:book-detail', kwargs={'pk': pk}))


class AuthorListAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer1


class AuthorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer2


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer1


class BookRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer2


class BookRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer3


class GenreListAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer2


class GenreRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer2


class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer2


def user_sign_out(request):
    next = request.GET.get('next')
    logout(request)
    return HttpResponseRedirect(next)


def user_sign_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    next = request.POST.get('next')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
    return HttpResponseRedirect(next)


def change_favorite_status(request, pk):
    book = Book.objects.get(id=pk)
    user = request.user
    if book in user.profile.favorite_books.all():
        user.profile.favorite_books.remove(book)
    else:
        user.profile.favorite_books.add(book)
    return HttpResponseRedirect(book.get_absolute_url())


def search(request):
    pattern = request.POST.get('pattern')
    next = request.POST.get('next')
    if pattern:
        books = Book.objects.filter(title__icontains=pattern)
        authors = Author.objects.filter(Q(last__icontains=pattern) | Q(first__icontains=pattern))
        genres = Genre.objects.filter(name__icontains=pattern)
        context = {
            'pattern': pattern,
            'books_res': books,
            'authors_res': authors,
            'genres_res': genres
        }
        return render(
            request,
            template_name='library/search.html',
            context=context
        )
    else:
        if next == reverse('library:search'):
            return HttpResponseRedirect(reverse('library:index'))
        else:
            return HttpResponseRedirect(next)


def add_new_author(request):
    f = AuthorForm(request.POST)
    new_author = f.save(commit=False)
    new_author.slug = f'{new_author.first}-{new_author.last}'
    new_author.save()
    return HttpResponseRedirect(reverse('library:author-list'))


def add_new_book(request):
    f = BookForm(request.POST, request.FILES)
    new_book = f.save(commit=False)
    new_book.cover = request.FILES.get('cover')
    new_book.save()
    f.save_m2m()
    return HttpResponseRedirect(new_book.get_absolute_url())


def user_creation_template(request):
    context = {
        'form': MyUserCreationForm()
    }
    return render(
        request,
        template_name='library/user.html',
        context=context
    )


def add_new_user(request):
    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if password1 == password2:
        user = User.objects.create_user(username=username, password=password1)
        Profile.objects.create(user=user, img=request.FILES.get('img'))
        login(request, user)
        return HttpResponseRedirect(reverse('library:index'))
    else:
        context = {
            'form': MyUserCreationForm(),
            'message': f'password1 and password2 doesnt match'
        }
        return render(
            request,
            template_name='library/user.html',
            context=context
        )
    return HttpResponseRedirect(reverse('library:user'))
