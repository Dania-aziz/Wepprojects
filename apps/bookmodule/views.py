from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Book, Student, Address, BookLab9, Publisher, Author  
from django.db.models import Count, Sum, Avg, Max, Min, Q  
from django.contrib.auth.decorators import login_required


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
 
def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8_task1.html', {'books': books})

def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/lab8_task2.html', {'books': books})

def lab8_task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=3) & ~(Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/lab8_task3.html', {'books': books})

def lab8_task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8_task4.html', {'books': books})

def lab8_task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/lab8_task5.html', {'stats': stats})

def lab8_task7(request):
    city_counts = Student.objects.values('address__city').annotate(student_count=Count('id'))
    return render(request, 'bookmodule/lab8_task7.html', {'city_counts': city_counts})

def lab9_task1(request):
    total_books = BookLab9.objects.aggregate(total=Count('id'))['total']

    books = BookLab9.objects.all()

    for book in books:
        book.percentage = (book.quantity / total_books) * 100 if total_books > 0 else 0

    return render(request, 'bookmodule/lab9_task1.html', {'books': books})

def lab9_task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('booklab9__quantity'))
    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})

def lab9_task3(request):
    authors = Author.objects.annotate(
        total_books=Count('booklab9')
    )

    return render(request, "bookmodule/lab9_task3.html", {"authors": authors})

def lab9_task4(request):
    authors = Author.objects.annotate(
        avg_price=Avg('booklab9__price')
    )

    return render(request, "bookmodule/lab9_task4.html", {"authors": authors})

def lab9_task5(request):
    authors = Author.objects.annotate(
        total_stock=Sum('booklab9__quantity')
    )

    return render(request, "bookmodule/lab9_task5.html", {"authors": authors})

@login_required
def lab9_task6(request):
    user = request.user
    return render(request, "bookmodule/lab9_task6.html", {"user": user})