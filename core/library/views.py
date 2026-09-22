from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.

def books_list (request):
    books = Books.objects.all()
    return render(request, 'books.html', {'books': books})

def books_details (request, book_id):
    books = get_object_or_404(Books, id=book_id)
    authors = get_object_or_404(Books.objects.select_related('authors'), id=book_id)
    return render(request, 'books_details.html', {'books': books, 'authors': authors})

def book_add (request):
    if request.method == "POST":
        title = request.POST.get('title', '').strip()
        authors = request.POST.get('authors', '').strip()
        author = Authors.objects.get(id=authors)
        isbn = request.POST.get('isbn', '').strip()
        publication_year = request.POST.get('publication_year', '').strip()
        genres = request.POST.get('genres', '').strip()
        co_author = request.POST.get('co_author', '').strip()
        summary = request.POST.get('summary', '').strip()
        books = Books (title=title, authors=author, isbn=isbn, publication_year=publication_year, genres=genres, co_author=co_author, summary=summary)
        books.save()
        return redirect('view_books')
    else:
        books = Books.objects.all()
        authors = Authors.objects.all()
        genres = Genres.objects.all()
    return render (request, 'books_add.html', {'books': books, 'authors': authors, 'genres': genres})