from django.urls import path
from . import views

app_name = 'bookmodule'

urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.html5_links, name='html5_links'),
    path('html5/text/formatting/', views.text_formatting, name='text_formatting'),
    path('html5/listing/', views.listing, name='listing'),
    path('html5/tables/', views.tables, name='tables'),
    path('search/', views.book_search, name='book_search'),
    path('simple/query/', views.simple_query, name='simple_query'),
    path('complex/query/', views.complex_query, name='complex_query'),
    path('lab8/task1', views.lab8_task1, name='lab8_task1'),
    path('lab8/task2', views.lab8_task2, name='lab8_task2'),
    path('lab8/task3', views.lab8_task3, name='lab8_task3'),
    path('lab8/task4', views.lab8_task4, name='lab8_task4'),
    path('lab8/task5', views.lab8_task5, name='lab8_task5'),
    path('lab8/task7', views.lab8_task7, name='lab8_task7'),
    path("lab9/task1", views.lab9_task1, name="lab9_task1"),
    path("lab9/task2", views.lab9_task2, name="lab9_task2"),
    path("lab9/task3", views.lab9_task3, name="lab9_task3"),
    path("lab9/task4", views.lab9_task4, name="lab9_task4"),
    path("lab9/task5", views.lab9_task5, name="lab9_task5"),
    path("lab9/task6", views.lab9_task6, name="lab9_task6"),

    ]