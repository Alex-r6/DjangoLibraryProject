from django.contrib import admin
from .models import *


class BookInLines(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['__str__', ]
    prepopulated_fields = {'slug': ['first', 'last']}
    inlines = [BookInLines]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_filter = ['author', ]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', ]


@admin.register(BookShop)
class BookShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'book_cover', 'quantity']
