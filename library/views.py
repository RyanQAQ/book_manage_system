import pymysql
from django.shortcuts import render, HttpResponse, redirect
from django.views import generic
from library.models import Publisher, Book, Sort


class IndexView(generic.ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'books'


def edit(request, edit_id):
    book_obj = Book.objects.get(id=edit_id)
    return render(request, 'edit.html', {'book_obj': book_obj})


def save_edit(request, edit_id):
    book_obj = Book.objects.get(id=edit_id)
    name = request.POST['name']
    price = request.POST['price']
    author = request.POST['author']
    publisher = request.POST['publisher']
    pubdate = request.POST['pubdate']
    sort = request.POST['sort']
    publisher_id = Publisher.objects.get(name=publisher).id
    sort_id = Sort.objects.get(name=sort).id

    conn = pymysql.connect(host='121.199.28.54', port=3306, user='root', passwd='lyk0915',
                           db='book_manage_sys', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "update books set name='{0}', price={1}, author='{2}', publisher_id={3}, pub_date='{4}', sort_id={5} " \
          "where id={6}".format(name,price,author,publisher_id,pubdate,sort_id,edit_id)
    print(sql)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')


def add(request):
    return render(request, 'add.html')