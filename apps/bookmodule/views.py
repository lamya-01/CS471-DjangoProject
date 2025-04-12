from django.shortcuts import render
from django.http import HttpResponse


def index(request): 
    return render(request, "bookmodule/index.html") 
def list_books(request): 
    return render(request, 'bookmodule/list_books.html') 
def viewbook(request, bookId): 
    return render(request, 'bookmodule/one_book.html') 
def aboutus(request): 
    return render(request, 'bookmodule/aboutus.html') 


def html5_links(request):
    return render(request, "bookmodule/html5_links.html")

def html5_text_formatting(request):
    return render(request, "bookmodule/html5_text_formatting.html")

def html5_listing(request):
    return render(request, "bookmodule/html5_listing.html")

def html5_tables(request):
    return render(request, "bookmodule/html5_tables.html")


def book_search(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        # Get book list
        books = __getBooksList()
        newBooks = []

        for book in books:
            contained  = False
            if isTitle and string in book['title'].lower():
                contained  = True
            if not contained  and isAuthor and string in book['author'].lower():
                contained  = True
            if contained :
                newBooks.append(book)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')

def __getBooksList(): 
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'} 
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'} 
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'} 
    return [book1, book2, book3]


from .models import Book 

#Use the constructor function
mybook = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 1) 
mybook.save()

#Use the create function
mybook = Book.objects.create(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', 
edition = 1) 



def simple_query(request): 
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects 
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def complex_query(request): 
   mybooks=Book.objects.filter(author__isnull = False # Filter books where 'author' is not null
    ).filter(title__icontains='and'# Filter books where the 'title' contains the word 'and' (case-insensitive)
    ).filter(edition__gte = 2 # Filter books where the 'edition' is greater than or equal to 2
    ).exclude(price__lte = 100 # Exclude books where the 'price' is less than or equal to 100
    )[:10] # Limit the results to the first 10 books

   if len(mybooks)>=1: 
      return render(request, 'bookmodule/bookList.html', {'books':mybooks}) 
   else: 
      return render(request, 'bookmodule/index.html')
   


from django.db.models import Q
from .models import Book

def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/task1.html', {'books': books})


def lab8_task2(request):
    books = Book.objects.filter(Q(edition__gt=3) & (Q(title__icontains='co') | Q(author__icontains='co')))
    return render(request, 'bookmodule/lab8_task2.html', {'books': books})


def lab8_task3(request):
    books = Book.objects.filter(~Q(edition__gt=3) & ~(Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/lab8_task3.html', {'books': books})


def lab8_task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8_task4.html', {'books': books})


from django.db.models import Count, Avg, Sum, Max, Min

def lab8_task5(request):
    data = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price'),
    )
    return render(request, 'bookmodule/lab8_task5.html', {'data': data})



from .models import Address, Student
# Create cities
city1 = Address.objects.create(city='Riyadh')
city2 = Address.objects.create(city='Jeddah')
city3 = Address.objects.create(city='Tabuk')
city4 = Address.objects.create(city='Taif')
city5 = Address.objects.create(city='Qassim')

# Create students
Student.objects.create(name='Sara', age=21, address=city1)
Student.objects.create(name='Ali', age=23, address=city2)
Student.objects.create(name='Lina', age=20, address=city1)
Student.objects.create(name='Mohammed', age=22, address=city2)
Student.objects.create(name='Lamya', age=24, address=city5)
Student.objects.create(name='layan', age=15, address=city2)
Student.objects.create(name='Fatima', age=26, address=city5)
Student.objects.create(name='Faras', age=22, address=city1)
Student.objects.create(name='Ahmad', age=28, address=city1)
Student.objects.create(name='Naif', age=22, address=city5)




from .models import Student
from django.db.models import Count

def city_count(request):
    counts = Student.objects.values('address__city').annotate(total=Count('id'))
    return render(request, 'bookmodule\city_count.html', {'counts': counts})