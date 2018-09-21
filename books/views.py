from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from books.forms import ContactForm, AuthorForm, AuthorSearchForm, LoginForm
from books.models import Book, Author

from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.contrib.auth import authenticate, login, logout

from django.views.generic import View


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append("Please enter a search term.")
        elif len(q) > 20:
            errors.append("Please enter at most 20 characters only.")
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(
                request,
                'search_results.html',
                {'books': books, 'query': q},
            )
    return render(request, 'search_form.html', {'errors': errors})

@login_required
def contact(request):
    errors = []
    if request.method == 'POST':  # If the form has been submitted...
        form = ContactForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            return HttpResponse('Thanks!')
    else:
        form = ContactForm()  # An unbound form

    return render(
        request,
        'contact.html',
        {'form': form, 'errors': errors}
    )


class ContactView(View):
    form_class = ContactForm
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.return_render(form=form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponse('Thanks!')
        else:
            errors = ["There is an error on your form"]
        self.return_render(form=form, errors=errors)

    def return_render(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            {'form': kwargs['form'], 'errors': kwargs['error']})




@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save()
            return HttpResponse("{author} is added in our database!".format(author=new_author))
    else:
        form = AuthorForm()
        
    return render (
        request,
        'add-author.html',
        {'form': form}
    )

@login_required
def search_author(request):
    form = AuthorSearchForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data['name']
        results = Author.objects.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
        return render(request, 'author-results.html', {'authors': results, 'query': name})
    else:
        form = AuthorSearchForm()
        error = True
        return render(request, 'author-search.html', {'error': error, 'form': form})



def login_view(request):
    errors = []
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Successfully logged in!")
                else:
                    errors.append("User is currently disabled")
            else:
                errors.append("Incorrect username or password")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'errors': errors})


def logout_view(request):
    logout(request)
    return HttpResponse("You have been logged out!")
