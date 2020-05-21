from django.shortcuts import render
from django. urls import reverse
from mainapp.models import Book, BookCategory, Published_books, Interesting_authors, Interesting_books
from django.http import JsonResponse
from django.template.loader import render_to_string
from authorization.models import ParkUser

# from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from robokassa.forms import RobokassaForm
# from __future__ import unicode_literals
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from robokassa.conf import USE_POST
from robokassa.forms import ResultURLForm, SuccessRedirectForm, FailRedirectForm
from robokassa.models import SuccessNotification
from robokassa.signals import result_received, success_page_visited, fail_page_visited

# from robokassa.signals import result_received
# from my_app.models import Order

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

@login_required
def product(request, order_id):
    return render(request, 'product.html', {'form': form})

    order = get_object_or_404(Order, pk=order_id)

form = RobokassaForm(initial={
    'OutSum': 'order_title',
    'InvId': 'order_id',
    'Desc': 'order_name',
    # 'Email': request.user.email,
    # 'IncCurrLabel': '',
    # 'Culture': 'ru'
})

# def payment_received(sender, **kwargs):
# order = Order.objects.get(id=kwargs['InvId'])
# order.status = 'paid'
# order.paid_sum = kwargs['OutSum']
# order.extra_param = kwargs['extra']['my_param']
# order.save()
#
# result_received.connect(payment_received)

@csrf_exempt
def receive_result(request):
    """Обработчик для ResultURL."""
    data = request.POST if USE_POST else request.GET
    form = ResultURLForm(data)
    if form.is_valid():
        inv_id, out_sum = form.cleaned_data['InvId'], form.cleaned_data['OutSum']

        # сохраняем данные об успешном уведомлении в базе, чтобы
        # можно было выполнить дополнительную проверку на странице успешного
        # заказа
        notification = SuccessNotification.objects.create(InvId=inv_id, OutSum=out_sum)

        return HttpResponse('OK%s' % inv_id)
    return HttpResponse('error: bad signature')


@csrf_exempt
def success(request, template_name='robokassa/success.html', extra_context=None,
            error_template_name='robokassa/error.html'):
    """Обработчик для SuccessURL"""

    data = request.POST if USE_POST else request.GET
    form = SuccessRedirectForm(data)
    if form.is_valid():
        inv_id, out_sum = form.cleaned_data['InvId'], form.cleaned_data['OutSum']

        # в случае, когда не используется строгая проверка, действия с заказом
        # можно осуществлять в обработчике сигнала robokassa.signals.success_page_visited
        success_page_visited.send(sender=form, InvId=inv_id, OutSum=out_sum,
                                  extra=form.extra_params())

        context = {'InvId': inv_id, 'OutSum': out_sum, 'form': form}
        context.update(form.extra_params())
        context.update(extra_context or {})
        return TemplateResponse(request, template_name, context)

    return TemplateResponse(request, error_template_name, {'form': form})


@csrf_exempt
def fail(request, template_name='robokassa/fail.html', extra_context=None,
         error_template_name='robokassa/error.html'):
    """Обработчик для FailURL"""

    data = request.POST if USE_POST else request.GET
    form = FailRedirectForm(data)
    if form.is_valid():
        inv_id, out_sum = form.cleaned_data['InvId'], form.cleaned_data['OutSum']

        # дополнительные действия с заказом (например, смену его статуса для
        # разблокировки товара на складе) можно осуществить в обработчике
        # сигнала robokassa.signals.fail_page_visited
        fail_page_visited.send(sender=form, InvId=inv_id, OutSum=out_sum,
                               extra=form.extra_params())

        context = {'InvId': inv_id, 'OutSum': out_sum, 'form': form}
        context.update(form.extra_params())
        context.update(extra_context or {})
        return TemplateResponse(request, template_name, context)

    return TemplateResponse(request, error_template_name, {'form': form})

def error(request):
    return render(request, 'mainapp/error.html')