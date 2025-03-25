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