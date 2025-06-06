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
path('lab10_part1/listbooks/' , views.lab10_part1_listbooks , name ='book.lab10_part1_listbooks'),
path('lab10_part1/addbook/',views.add_book,name='book.add_book'),
path('lab10_part1/editbook/<int:id>',views.edit_book,name='book.edit_book'),
path('lab10_part1/deletebook/<int:id>',views.delete_book,name='book.delete_book'),

path('lab10_part2/listbooks/' , views.lab10_part2_listbooks , name ='book.lab10_part2_listbooks'),
path('lab10_part2/addbook/',views.lab10_part2_addbook,name='book.lab10_part2_addbook'),
path('lab10_part2/editbook/<int:id>',views.lab10_part2_editbook,name='book.lab10_part2_editbook'),
path('lab10_part2/deletebook/<int:id>',views.lab10_part2_deletebook,name='book.lab10_part2_deletebook'),

path('lab11/liststudent/', views.lab11_list_students, name='book.lab11_list_students'),
path('lab11/addstudent/', views.lab11_add_student, name='book.lab11_add_student'),
path('lab11/updatestudent/<int:student_id>/', views.lab11_update_student, name='book.lab11_update_student'),
path('lab11/deletestudent/<int:student_id>/', views.lab11_delete_student, name='book.lab11_delete_student'),

path('lab11T2/liststudent/', views.lab11T2_list_students, name='book.lab11T2_list_students'),
path('lab11T2/addstudent/', views.lab11T2_add_student, name='book.lab11T2_add_student'),
path('lab11T2/updatestudent/<int:student_id>/', views.lab11T2_update_student, name='book.lab11T2_update_student'),
path('lab11T2/deletestudent/<int:student_id>/', views.lab11T2_delete_student, name='book.lab11T2_delete_student'),

path('lab11T3/listbook/', views.lab11T3_listbooks, name='book.lab11T3_listbooks'),
path('lab11T3/addbook/', views.lab11T3_addBook, name='book.lab11T3_addBook'),
] 