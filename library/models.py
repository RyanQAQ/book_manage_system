from django.db import models
import datetime


class Publisher(models.Model):
    name = models.CharField(max_length=10, verbose_name='出版社名字')
    city = models.CharField(max_length=6, verbose_name='出版社所在城市')

    class Meta:
        db_table = 'publishers'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name


class Sort(models.Model):
    name = models.CharField(max_length=6, verbose_name='分类名')

    class Meta:
        db_table = 'sort'
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Book(models.Model):
    name = models.CharField(max_length=10, verbose_name='书名')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='价格')
    author = models.CharField(max_length=10, verbose_name='作者')
    pub_date = models.DateField(default=datetime.date, verbose_name='出版日期')
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, verbose_name='出版社')
    sort = models.ForeignKey(Sort, on_delete=models.PROTECT, verbose_name='分类')

    class Meta:
        db_table = 'books'
        verbose_name = '书籍'
        verbose_name_plural = verbose_name
