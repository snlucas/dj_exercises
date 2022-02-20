from django.test import TestCase
from .models import Book


class BookTestCase(TestCase):
    def setUp(self) -> None:
        test_book = Book.objects.create(
            title="Title 01", 
            subtitle="Subtitle 01",
            author="Author 01",
            price=25.00
        )
        test_book.save()

    def test_book_details(self):
        book = Book.objects.get(pk=1)
        title = f"{book.title}"
        subtitle = f"{book.subtitle}"
        author = f"{book.author}"
        price = f"{book.price}"
        self.assertEqual(title, "Title 01")
        self.assertEqual(subtitle, "Subtitle 01")
        self.assertEqual(author, "Author 01")
        self.assertEqual(price, "25.00")
