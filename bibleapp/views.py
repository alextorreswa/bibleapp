# from django.shortcuts import render

# # Create your views here.
# from django.views.generic import ListView
# from .models import BibleVersionKey

# class BookListView(ListView):
#     model = BibleVersionKey
#     template_name = 'bibleapp/book_list.html'
#     context_object_name = 'books'

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import BookInfo, Allbibles
from django.urls import reverse

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


def read(request, idbible, b, c):
  template = loader.get_template('read.html')  
  books = BookInfo.objects.all().values()
  if request.method == 'POST':
    # breakpoint()
    idBible = request.POST['version']
    idBook = request.POST['book']
    c = request.POST['chapter']
    allBibles = Allbibles.objects.filter(b=int(idBook), idbible=idBible, c=c)    
  else:
    allBibles = Allbibles.objects.filter(b=b, idbible=idbible, c=c)  
  context = {
    'allBibles': allBibles,
    'books': books,
  }      


  # breakpoint()
  return HttpResponse(template.render(context, request))

# def readSelect(request):
#   idBible=request.Get['Versions']
#   breakpoint()
#   read(request, idBible, 1, 1)