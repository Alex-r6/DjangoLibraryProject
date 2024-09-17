from django.test import TestCase
from .models import *


class AuthorTestCase(TestCase):
    def setUp(self) -> None:
        self.a1 = Author.objects.create(first='Vasay', last='Petrov')
        self.a2 = Author.objects.create(first='Petya', last='Mokin')
        self.a3 = Author.objects.create(first='ketya', last='Nokin')
        self.b1 = Book.objects.create(title='blabla', author=self.a1)
        self.b2 = Book.objects.create(title='blabla', author=self.a1)
        self.b3 = Book.objects.create(title='blabla', author=self.a2)

    def test1(self):
        '''провер. кол-ва обьектов'''
        self.assertTrue(Author.objects.exists())
        n = Author.objects.count()
        self.assertEqual(n, 3)
        n1 = Author.objects.filter(first__startswith='v').count()
        self.assertEqual(n1, 1)

    def test2(self):
        '''провер. метод __str__'''
        s1 = str(self.a1)
        self.assertEqual(s1, 'Vasay Petrov')
        s2 = self.a2.__str__()
        self.assertEqual(s2, 'Petya Mokin')
        s3 = str(self.b1)
        self.assertEqual(s3, self.b1.title)

    def test3(self):
        '''провер. связей'''
        self.assertEqual(self.b1.author, self.a1)
        n1 = self.a1.books.count()
        n2 = Book.objects.filter(author=self.a2).count()
        n3 = self.b1.genres.count()
        self.assertEqual(n1, 2)
        self.assertEqual(n2, 1)
        self.assertEqual(n3, 0)
        self.assertFalse(self.b1.genres.exists())
        self.assertTrue(self.a1.books.exists())
        self.assertFalse(self.a3.books.exists())