from django.urls import path 

from . import views 
#urlpatterns = [
#path('', views.index), 
#path('index2/<int:val1>/', views.index2),
#path('<int:bookId>', views.viewbook)
#] 

urlpatterns = [ 
path('', views.index, name= "books.index"), 
path('list_books/', views.list_books, name= "books.list_books"), 
path('<int:bookId>/', views.viewbook, name="books.view_one_book"), 
path('aboutus/', views.aboutus, name="books.aboutus"), 
path("html5/links/", views.html5_links, name="books.html5_links"),
path("html5/text/formatting/", views.html5_text_formatting, name="books.html5_text_formatting"),
path("html5/listing/", views.html5_listing, name="books.html5_listing"),
path("html5/tables/", views.html5_tables, name="books.html5_tables"),
path("search/", views.book_search, name="books.book_search"),
path("simple/query",views.simple_query, name="books.simple_query"),
path("complex/query",views.complex_query, name= "books.complex_query"),
path("lab8/task1/", views.lab8_task1, name="book.lab8_task1"),
path("lab8/task2/", views.lab8_task2, name="book.lab8_task2"),
path("lab8/task3/", views.lab8_task3, name="book.lab8_task3"),
path("lab8/task3/", views.lab8_task3, name="book.lab8_task3"),
path("lab8/task3/", views.lab8_task3, name="book.lab8_task3"),
path("lab8/task4/", views.lab8_task4, name="book.lab8_task4"),
path("lab8/task5/", views.lab8_task5, name="book.lab8_task5"),
path('students/city-count/', views.city_count, name='book.city_count'),
path('lab9/task1/', views.lab9_task1, name='book.lab9_task1'),
path('lab9/task2/', views.lab9_task2, name='book.lab9_task2'),
path('lab9/task3/', views.lab9_task3, name='book.lab9_task3'),
path('lab9/task4/', views.lab9_task4, name='book.lab9_task4'),
] 