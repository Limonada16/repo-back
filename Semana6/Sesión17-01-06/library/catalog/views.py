from .models import Author, Book
from django.shortcuts import redirect, render
from catalog.forms import ModelBookForm
from django.views.generic import CreateView
# from catalog.filters import split_name

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

def new_books(request):
    if request.method == 'POST':
        data = request.POST

        book = Book()
        book.title = data['title']
        book.autor = data['autor']
        book.editorial = data['editorial']
        book.year = data['year']
        book.volume = data['volume']
        book.save()

        return redirect('/catalog/')
    else:
        form = ModelBookForm()
        return render(request, 'catalog/new.html', {"form":form})


def get_books_by_editorial(request, editorial):
    books = Book.objects.filter(editorial = editorial)
    year = request.GET.get("year")
    print(year)
    if year != None:
        books = books.filter(year=year)

    return render(request,'catalog/index.html',{'books':books})
# Create your views here.
def catalog_list(request):
    books = Book.objects.all()
    return render(request,'catalog/index.html',{'books':books})
