from django.contrib import admin
from .models import Book, Publisher, Sort


admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Sort)
