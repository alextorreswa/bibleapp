# from django.shortcuts import render

# # Create your views here.
# from django.views.generic import ListView
# from .models import BibleVersionKey

# class BookListView(ListView):
#     model = BibleVersionKey
#     template_name = 'bibleapp/book_list.html'
#     context_object_name = 'books'

from django.http import HttpResponse
from django.template import loader
from .models import BookInfo

def books(request):
  books = BookInfo.objects.all().values()
  template = loader.get_template('books.html')
  context = {
    'books': books,
  }
  return HttpResponse(template.render(context, request))
  
def book(request, id):
  book = BookInfo.objects.get(order=id)
  template = loader.get_template('book.html')
  context = {
    'book': book,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def read(request):
  books = BookInfo.objects.all().values()
  template = loader.get_template('read.html')
  context = {
    'books': books,
  }
  return HttpResponse(template.render(context, request))

