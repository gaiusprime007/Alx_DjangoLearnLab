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
from django.http import HttpResponse

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    #authentication and authorization
    path('login-alt/', LoginView.as_view(template_name = 'relationship_app/login.html'), name='login'),
    path('logout/',  LogoutView.as_view(template_name = 'relationship_app/login.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
