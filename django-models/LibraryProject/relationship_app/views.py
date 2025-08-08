from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import DetailView
from django.http import HttpResponse
from django.contrib.auth import authenticate  
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


def test_view(request):
    return HttpResponse("Test URL is working!")


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        return context
    # AUTHENTICATION AND AUTHORIZATION
   
   
   
   
   
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form =  UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.get_user()
            login(request, username)
            messages.success(request, 'Login successful!')
            return redirect('book_list')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})
        
    
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return render(request, 'relationship_app/logout.html')