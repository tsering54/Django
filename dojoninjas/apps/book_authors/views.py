# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from . models import Book, Author

# Create your views here.
def index(request):
    return render(request, 'book_authors/index.html')

def process(request):
    # newbook = Book.objects.create(
    #     name = request.POST['name'],
    #     desc = request.POST['desc']
    # )

    # newauthor = Author.objects.create(
    #     first_name = request.POST['first_name'],
    #     last_name = request.POST['last_name'],
    #     email = request.POST['email']
    # )

    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'all_books' = books,
        'all_authors' = authors,
    }
    return render(request, 'book_authors/index.html', context)