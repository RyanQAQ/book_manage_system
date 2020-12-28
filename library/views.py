import pymysql
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.views import generic
from library.models import Publisher, Book, Sort, User


def required_login(func):
    def inner(*args, **kwargs):
        request = args[0]
        if request.session.get('username'):
            return func(*args, **kwargs)
        else:
            return redirect('/login/')
    return inner


class IndexView(generic.ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'books'


@required_login
def edit(request, edit_id):
    book_obj = Book.objects.get(id=edit_id)
    return render(request, 'edit.html', {'book_obj': book_obj})


@required_login
def save_edit(request, edit_id):
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
          "where id={6};".format(name,price,author,publisher_id,pubdate,sort_id,edit_id)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')


@required_login
def add(request):
    return render(request, 'add.html')


@required_login
def save_add(request):
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
    sql = "insert into books(name, price, author, publisher_id, pub_date, sort_id) values ('{0}', {1}, '{2}', {3}, '{4}', {5});".format(name, price, author, publisher_id, pubdate, sort_id)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')


@required_login
def del_book(request, del_id):
    b = Book.objects.get(id=del_id)
    print('bbb', b)
    b.delete()
    return HttpResponseRedirect('/')


def login(request):
    return render(request, 'login.html', {'hint': ''})


def signin(request):
    user = request.POST.get('inputName')
    passwd = request.POST.get('inputPassword')

    username = User.objects.get(id=1).username
    password = User.objects.get(id=1).password

    if request.method == 'GET':
        return render(request, 'login.html', {'hint': ''})
    else:
        if user == username and passwd == password:
            request.session['username'] = user
            print(request.session['username'])
            return redirect('/')
        else:
            return render(request, 'login.html', {'hint': '用户名或密码错误，请重新登录！'})


def logout(request):
    request.session.flush()
    return redirect('/')
