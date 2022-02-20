from django.shortcuts import render, HttpResponse, redirect, reverse
from django.views import View

from biblioteczka_app.forms import AddBookForm
from biblioteczka_app.models import Author, Book


# Create your views here.
class Blank(View):
    def get(self, request):
        message = 'To jest wiadomość'
        return render(request, 'blank.html',
                      {'message': message})


class AddAuthor(View):
    def get(self, request):
        return render(request, 'add_author.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        Author.objects.create(first_name=first_name, last_name=last_name)
        return HttpResponse('Dodano autora')

    # return redirect(reverse('add'))


class AuthorDisplay(View):
    def get(self, requests):
        authors = Author.objects.all()
        return render(requests, 'author_list.html', {'authors': authors})


class AuthorId(View):
    def get(self, request, id):
        author = Author.objects.get(id=id)
        return render(request, 'author.html', {'author': author})


class AddBook(View):
    def get(self, request):
        form = AddBookForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AddBookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            year = form.cleaned_data['year']
            author = form.cleaned_data['author']
            Book.objects.create(title=title, year=year, author=author)
            return redirect('add_book')
        return render(request, 'form.html', {'form': form})
