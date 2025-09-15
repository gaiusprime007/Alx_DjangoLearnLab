# from django.urls import path
# from . import views


# urlpatterns = [
#     path('test/', views.test_view, name="test_view"),
#     path('books/', views.book_list, name = 'book_list'),
#     path('library/<int:pk>', views.LibraryDetailView.as_view(), name='library_detail'),
#     path('register/', views.register_view, name='register'),
#     path('login/', views.login_view, name= 'login'),
#     path('logout/', views.logout_view, name='logout'),
# ]


print ("loaded relationship_app urls.py")

from django.urls import path
from . import views
from .views import LoginView
from .views import LogoutView
from .views import RegisterView
from .views import AddBookView
from .views import EditBookView
from .views import DeleteBookView


urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('books/add/', AddBookView.as_view(), name='add_book'),
    path('books/<int:pk>/edit/', EditBookView.as_view(), name='edit_book'),
    path('books/<int:pk>/delete/', DeleteBookView.as_view(), name='delete_book'),

    #authentication and authorization
    path('login-alt/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
    path('logout/',  LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),
    path('register/', RegisterView.as_view(template_name="relationship_app/register.html"), name='register'),

    #access control
    path('admin-dashboard/', views.admin_view, name='admin_view.html'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_view.html'),
    path('member-dashboard/', views.member_view, name='member_view.html'),

]
