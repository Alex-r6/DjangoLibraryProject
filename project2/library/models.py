from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Author(models.Model):
    first = models.CharField(max_length=25)
    last = models.CharField(max_length=25)
    info = models.TextField(blank=True)
    portrait = models.URLField(blank=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return f"{self.first} {self.last}"

    def comments(self):
        return Comment.objects.filter(book__author__id=self.id).select_related('book').all()

    def get_absolute_url(self):
        return reverse('library:author-detail', kwargs={'slug': self.slug})


class Book(models.Model):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='covers/', blank=True)
    desc = models.TextField(blank=True)
    genres = models.ManyToManyField('Genre', related_name='books', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library:book-detail', kwargs={'pk': self.id})


class Genre(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Comment(models.Model):
    username = models.CharField(max_length=15)
    text = models.CharField(max_length=150)
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    created = models.DateTimeField(default=now)

    class Meta:
        ordering = ['-created']


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='user_img/', blank=True)
    favorite_books = models.ManyToManyField(Book, related_name="fans", blank=True)

    def __str__(self):
        return self.user.username


class BookShop(models.Model):
    name = models.ForeignKey(Book, related_name='shop', on_delete=models.CASCADE)
    price = models.FloatField(default=1.00)
    book_cover = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)