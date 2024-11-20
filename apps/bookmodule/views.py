from django.shortcuts import render,redirect
from .models import Book,Address,Student
from django.db.models import Q,Min,Max,Avg,Count,Sum


def index2(request, val1 = 0):
    return render(request, "bookmodule/index2.html", {"value":val1})

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html', {"bookId":bookId})

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, 'bookmodule/links.html')

def formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained: newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
    else:
        return render(request, 'bookmodule/search.html')

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 50)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')


def task1(request):
    books = Book.objects.filter(Q(price__lte = 60))
    return render(request, 'bookmodule/bookList.html', {'books':books})

def task2(request):
    books =  Book.objects.filter(Q(edition__gt = 2)&(Q(title__contains = 'qu') | Q(author__contains = 'qu')) )
    return render(request, 'bookmodule/bookList.html', {'books':books})

def task3(request):
    books =  Book.objects.filter( ~Q(edition__gt = 2)&(~ Q(title__contains = 'qu') | ~ Q(author__contains = 'qu')) )
    return render(request, 'bookmodule/bookList.html', {'books':books})

def task4(request):
    books = Book.objects.order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books':books})

def task5(request):
    #query = Book.objects.aggregate(count = Count('id',default=0), total=Sum('price', default=0), average=Avg('price',default=0), max=Max('price',default=0), =Min('price',default=0))
    count = Book.objects.aggregate(Count('id'))
    sum = Book.objects.aggregate(Sum('price', default=0))
    avg = Book.objects.aggregate(Avg('price', default=0))
    max = Book.objects.aggregate(Max('price', default=0))
    min = Book.objects.aggregate(Min('price', default=0))
    print (count,sum,max)
    return render(request, 'bookmodule/task5.html', {'count':count , 'sum':sum ,'avg':avg,'max':max,'min':min})

def task7(request):
    objs = Address.objects.annotate( count=Count('student'))
    return render(request, 'bookmodule/task7.html', {'objs':objs})

#lab 9------------------------------------------part1
def listbooks(request) :
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab9list.html', {'books':books})

def addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return redirect('listbooks')
    return render(request, 'bookmodule/lab9add.html')


def editbook(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.edition = request.POST.get('edition')
        book.save()
        return redirect('listbooks')
    return render(request, 'bookmodule/lab9edit.html', {'book': book})

def deletebook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('listbooks')

from .forms import BookForm
#lab 9------------------------------------------part2
def listbooksform(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab9listform.html', {'books': books})

def addbookform(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listbooksform')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab9addform.html', {'form': form})

def editbookform(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('listbooksform')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab9editform.html', {'form': form, 'book': book})


