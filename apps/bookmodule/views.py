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
