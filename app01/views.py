from django.shortcuts import render,HttpResponse,redirect
from django.core.urlresolvers import reverse
from app01 import models
import time
# Create your views here.
def login(request):
    err_msg = ''
    if request.method == 'POST':
        name = request.POST.get("name12")
        pwd = request.POST.get("pwd12")
        if name == 'lary' and pwd == '123456':
            return redirect(reverse('my_bookList'),)
        else:
            err_msg = 'name or pwd wrong!'
    return render(request, 'login.html', {"error": err_msg})

def book_list(request):
    books = models.Book.objects.all()
    return render(request, 'book_list.html', locals())

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        date = request.POST.get('date')
        memo = request.POST.get('memo')
        publish_id = request.POST.get('inlineRadioOptions')
        author_id_list = request.POST.getlist('author_id_list')
        obj = models.Book.objects.create(title=title, price=price, create_time=date, memo=memo, publish_id=publish_id)
        obj.author.add(*author_id_list)

        return redirect(reverse('my_bookList'),)
    else:
        publish_list = models.Publish.objects.all()
        author_list = models.Author.objects.all()
        return render(request,'add_book.html', locals())

def delete_book(request, id):
    models.Book.objects.filter(id=id).delete()
    return redirect(reverse('my_bookList'),)

def edit_book(request,id):
    book = models.Book.objects.get(id=id)
    # 获取book的author列表
    book_author_l = []
    book_authors = book.author.all()
    for book_author in book_authors:
        book_author_l.append(book_author.id)

    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        date = request.POST.get('date')
        memo = request.POST.get('memo')
        publish_id = request.POST.get('inlineRadioOptions')
        author_id_list = request.POST.getlist('author_id_list')
        print(author_id_list)

        book.title = title
        book.price = price
        book.date =date
        book.memo =memo
        book.publish_id =publish_id

        book.author.set(author_id_list)
        book.save()
        # book.author.add(*author_id_list)
        return redirect(reverse('my_bookList'),)

    publish_list = models.Publish.objects.all()
    # 获取所有author列表
    author_list = models.Author.objects.all()

    return render(request, 'edit_book.html', locals())
