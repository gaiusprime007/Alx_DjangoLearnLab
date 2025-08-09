from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import DetailView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# def test_view(request):
#     return HttpResponse("Test URL is working!")


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
