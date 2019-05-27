from django.contrib import admin
from mainapp.models import Book, BookCategory, Published_books, Interesting_books, Interesting_authors

admin.site.register(Book)
admin.site.register(BookCategory)
admin.site.register(Published_books)
admin.site.register(Interesting_books)
admin.site.register(Interesting_authors)