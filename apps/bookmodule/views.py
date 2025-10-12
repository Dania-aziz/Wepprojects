from django.http import HttpResponse, Http404
from django.shortcuts import render


def tables(request):
    return render(request, 'books/html5_tables.html')


def listing(request):
    return render(request, 'books/html5_listing.html')

def text_formatting(request):
    return render(request, 'books/html5_text_formatting.html')


def html5_links(request):
    return render(request, 'books/html5_links.html')

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Internet & World Wide Web How to Program', 'author': 'author name'}
    book2 = {'id': 456, 'title': 'C++ How to Program, Late Objects Version', 'author': 'author name'}
    book3 = {'id': 789, 'title': 'Images in Another Folder', 'author': 'author name'}

    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    elif book2['id'] == bookId:
        targetBook = book2
    elif book3['id'] == bookId:
        targetBook = book3

    if not targetBook:
        raise Http404("Book not found")

    return render(request, 'bookmodule/one_book.html', {'book': targetBook})