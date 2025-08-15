from django.shortcuts import get_object_or_404, redirect, render
from .models import Book

from .models import Library
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})



## RESTRICTIONS SETTINGS
@method_decorator(permission_required('relationship_app.can_add_book', raise_exception=True), name='dispatch')
class AddBookView(CreateView):
    model = Book
    fields =['title', 'author', 'published_date',]
    template_name = 'relationship_app/add_book.html'
    success_url = reverse_lazy('book_list')

@method_decorator(permission_required('relationship_app.can_change_book', raise_exception=True), name='dispatch')
class EditBookView(UpdateView):
    model = Book
    fields = ['title', 'author', 'published_date']
    template_name = 'relationship_app/edit_book.html'
    success_url = reverse_lazy('book_list')


@method_decorator(permission_required('relationship_app.can_delete_book', raise_exception=True), name='dispatch')
class DeleteBookView(DeleteView):
    model = Book
    template_name = 'relationship_app/delete_book.html'
    success_url = reverse_lazy('book_list')


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        return context


    # AUTHENTICATION AND AUTHORIZATION

class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserCreationForm()
        return context

    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Registration successful!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Registration failed. Please correct the errors below')
        return super().form_invalid(form)




# class RegisterView(RegisterView):

class LoginView(LoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, 'Login successful!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return super().form_invalid(form)


class LogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
    reverse_lazy = 'login'

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'You have been logged out successfully.')
        return super().dispatch(request, *args, **kwargs)


