from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Book

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

def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

def book_search(request):

    if request.method == "POST":

        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1') == 'on' 
        isAuthor = request.POST.get('option2') == 'on'
        
        books = Book.objects.all()
        newBooks = []
        
        for item in books:
            contained = False
            if isTitle and string in item.title.lower(): 
                contained = True
            if not contained and isAuthor and string in item.author.lower(): 
                contained = True
            if contained: 
                newBooks.append(item)
        
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
    
    return render(request, 'bookmodule/search.html')

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='the')  
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(
        author__isnull=False
    ).filter(
        title__icontains='the'  
    ).filter(
        edition__gte=2
    ).exclude(
        price__lte=100
    )[:10]
    
    if mybooks.exists():
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
      
        return render(request, 'bookmodule/bookList.html', {'books': []})