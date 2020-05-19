"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
import mainapp.views as mainapp

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('categories/', mainapp.categories, name='categories'),
    path('Interesting_facts_in_the_world_of_books/', mainapp.Interesting_facts_in_the_world_of_books, name='Interesting_facts_in_the_world_of_books'),
    path('Recently_published_books/', mainapp.Recently_published_books, name='Recently_published_books'),
    path('The_authors/', mainapp.The_authors, name='The_authors'),
    path('Top_interesting_authors/', mainapp.Top_interesting_authors, name='Top_interesting_authors'),
    path('Top_interesting_books/', mainapp.Top_interesting_books, name='Top_interesting_books'),
    path('Bookstore/', mainapp.Bookstore, name='Bookstore'),
    path('delivery/', mainapp.delivery, name='delivery'),
    path('product/', mainapp.product, name='product'),
    path('we/', mainapp.we, name='we'),


    re_path('^categories/book/(\d+)/ajax/$', mainapp.categories_book_ajax),
    re_path('^categories/book-categories/(\d+)/ajax/$', mainapp.bookCategories_ajax),

    path('admin/', admin.site.urls),

    re_path('^auth/', include('authorization.urls', namespace='auth')),
    re_path('^map5/', include('chatapp.urls', namespace='chat')),
    re_path('^rkassa/', include('robokassa.urls', namespace='rkassa'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
