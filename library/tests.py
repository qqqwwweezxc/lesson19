from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class BookTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345678'
        )
        self.user.is_staff = True
        self.user.save()
        self.book = Book.objects.create(
            title='Book 1',
            author='Test Author',
            genre='Fiction',
            publication_year=1999,
        )

        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book.id])
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_get_books_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Book 1")

    def test_create_book(self):
        data = {
            "title": "Book 2",
            "author": "Test Author 2",
            "genre": "Drama",
            "publication_year": 1959,
        }

        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
