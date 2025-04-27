from django.shortcuts import render
from django.shortcuts import redirect
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




#lab9
from .models import Course , Student1 ,Department , Card
from django.db import connection

if Department.objects.count() == 0 and Student1.objects.count() == 0 and Card.objects.count() == 0 and Course.objects.count() == 0:
   # Create departments
   cs = Department.objects.create(name='Computer Science')
   math = Department.objects.create(name='Mathematics')
   Eng = Department.objects.create(name='English')

   # Create cards
   card1 = Card.objects.create(card_number=1111)
   card2 = Card.objects.create(card_number=2222)
   card3 = Card.objects.create(card_number=3333)
   card4 = Card.objects.create(card_number=4444)
   card5 = Card.objects.create(card_number=5555)
   card6 = Card.objects.create(card_number=6666)
   card7 = Card.objects.create(card_number=7777)
   card8 = Card.objects.create(card_number=8888)

   # Create courses
   course1 = Course.objects.create(title='Web Development', code=101)
   course2 = Course.objects.create(title='Algorithms', code=102)
   course3 = Course.objects.create(title='AI', code=103)
   course4 = Course.objects.create(title='Eng101', code=105)
   course5 = Course.objects.create(title='Calculus', code=107)


   # Create students
   student1 = Student1.objects.create(name='Lamya', card=card1, department=cs)
   student2 = Student1.objects.create(name='Fay', card=card2, department=math)
   student3 = Student1.objects.create(name='Bayan', card=card3, department=Eng)
   student4 = Student1.objects.create(name='Mona', card=card4, department=cs)
   student5 = Student1.objects.create(name='Layan', card=card5, department=cs)
   student6 = Student1.objects.create(name='Raghad', card=card6, department=math)
   student7 = Student1.objects.create(name='Mariam', card=card7, department=cs)
   student8 = Student1.objects.create(name='Rana', card=card8, department=Eng)

   # Assign courses (Many-to-Many)
   student1.course.add(course1, course2)
   student2.course.add(course5)
   student3.course.add(course4)
   student4.course.add(course1,course3,course5)
   student5.course.add(course2,course3)
   student6.course.add(course5)
   student7.course.add(course1,course3,course4)
   student8.course.add(course4)


from django.db.models import Count

def lab9_task1(request):
    departments = Department.objects.annotate(student_count=Count('student1'))
    return render(request, 'bookmodule\lab9_task1.html', {'departments': departments})

def lab9_task2(request):
    courses = Course.objects.annotate(student_count=Count('student1'))
    return render(request, 'bookmodule\lab9_task2.html', {'courses': courses})


from django.db.models import Min

def lab9_task3(request):
    departments = Department.objects.annotate(oldest_student_id = Min('student1__id'))
    return render(request, 'bookmodule\lab9_task3.html', {'departments':departments})


def lab9_task4(request):
    departments = Department.objects.annotate(student_count=Count('student1')) \
        .filter(student_count__gt=2).order_by('-student_count')#highest to lowest
    return render(request, 'bookmodule\lab9_task4.html', {'departments': departments})



def lab10_part1_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule\lab10_part1_listbooks.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            price=request.POST.get('price'),
            edition=request.POST.get('edition'),
        )
        return redirect('book.lab10_part1_listbooks')
    return render(request, 'bookmodule\lab10_part1_addbook.html')


def edit_book(request , id):
     book = Book.objects.get(id=id)
     if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price=request.POST.get('price')
        book.edition=request.POST.get('edition')
        book.save()
        return redirect('book.lab10_part1_listbooks')
     return render(request, 'bookmodule\lab10_part1_editbook.html', {'book': book})



def delete_book(request, id):
    book = Book.objects.get(id=id).delete()
    return redirect('book.lab10_part1_listbooks')



from .models import Book
from .forms import BookForm

def lab10_part2_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule\lab10_part2_listbooks.html', {'books': books})

def lab10_part2_addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book.lab10_part2_listbooks')
    else:
        form = BookForm()
        #form = forms.Book.BookForm(None)
    return render(request, 'bookmodule\lab10_part2_addbook.html', {'form': form})

def lab10_part2_editbook(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book.lab10_part2_listbooks')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule\lab10_part2_editbook.html', {'form': form})

def lab10_part2_deletebook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('book.lab10_part2_listbooks')
