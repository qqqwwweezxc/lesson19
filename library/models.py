from django.db import models


class Book(models.Model):
    """A class to represent a book"""
    title: str = models.CharField(max_length=255)
    author: str = models.CharField(max_length=255)
    genre: str = models.CharField(max_length=100)
    publication_year: int = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title