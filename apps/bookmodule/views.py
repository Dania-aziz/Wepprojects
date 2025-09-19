from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))


def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}

        
    targetBook = None

   # غير طريقة المقارنة هنا:
    if int(bookId) == book1['id']:
        targetBook = book1
    elif int(bookId) == book2['id']:
        targetBook = book2
    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)
