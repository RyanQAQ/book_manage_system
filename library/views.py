from django.conf import settings
from django.views import generic
from library.models import Publisher, Book, Sort


class IndexView(generic.ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'books'

