from django.shortcuts import render
from django. urls import reverse
from mainapp.models import Book, BookCategory, Published_books, Interesting_authors, Interesting_books

def index(request):
    return render(request, 'mainapp/index.html')

def categories(request):
    book_categories = BookCategory.objects.all()
    books = Book.objects.all()

    context = {
        'book_categories': book_categories,
        'books': books,
    }
    return render(request, 'mainapp/categories.html', context)

def Interesting_facts_in_the_world_of_books(reguest):
    return render(reguest, 'mainapp/Interesting_facts_in_the_world_of_books.html')

def Recently_published_books(reguest):
    published_books = Published_books.objects.all()

    context = {
        'published_books': published_books,
    }
    return render(reguest, 'mainapp/Recently_published_books.html', context)

def The_authors(reguest):
    return render(reguest, 'mainapp/The_authors.html')

def Top_interesting_authors(reguest):
    interesting_authors = Interesting_authors.objects.all()

    context = {
        'interesting_authors': interesting_authors,
    }
    return render(reguest, 'mainapp/Top_interesting_authors.html', context)

def Top_interesting_books(reguest):
    interesting_books = Interesting_books.objects.all()

    context = {
        'interesting_books': interesting_books,
    }
    return render(reguest, 'mainapp/Top_interesting_books.html', context)

