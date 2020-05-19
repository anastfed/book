from django.shortcuts import render
from django. urls import reverse
from mainapp.models import Book, BookCategory, Published_books, Interesting_authors, Interesting_books
from django.http import JsonResponse
from django.template.loader import render_to_string
from authorization.models import ParkUser

def index(request):
    peoples = []
    if request.user.is_authenticated:
        peoples = ParkUser.objects.exclude(pk=request.user.pk).order_by('last_name', 'first_name')
    context = {

        'peoples': peoples,
    }
    return render(request, 'mainapp/index.html', context)

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

def categories_book_ajax(request, book_pk):
    if request.is_ajax():
        current_book = Book.objects.filter(pk=book_pk).first()

        context = {
            'book_description': current_book.description

        }
        current_book_description = render_to_string('mainapp/book_desc.html', context)
        print('клик на книге передали контроллеру', book_pk)
        print(f'книга: {current_book.title}')

        context = {
            'current_book': current_book.title,
            'book_description': current_book_description,
        }
        return JsonResponse(context)


def bookCategories_ajax(request, categories_pk):
    if request.is_ajax():
        current_bookCategory = BookCategory.objects.filter(pk=categories_pk).first()

        context = {
            'bookCategory_description': current_bookCategory.description

        }

        current_bookCategory_description = render_to_string('mainapp/book_categories_desc.html', context)
        print(current_bookCategory_description)
        print(f'книга: {current_bookCategory.name}')

        context = {
            'current_bookCategory': current_bookCategory.name,
            'bookCategory_description': current_bookCategory_description,
        }
        return JsonResponse(context)

def Bookstore(request):

    return render(request, 'mainapp/Bookstore.html')


def delivery(request):

    return render(request, 'mainapp/delivery.html')


def product(request):

    return render(request, 'mainapp/product.html')


def we(request):

    return render(request, 'mainapp/we.html')

