from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def books_list (request):
    books = Books.objects.all()
    return render(request, 'books.html', {'books': books})

def books_details (request, book_id):
    books = get_object_or_404(Books, id=book_id)
    authors = get_object_or_404(Books.objects.select_related('authors'), id=book_id)
    return render(request, 'books_details.html', {'books': books, 'authors': authors})

# def book_add (request, )