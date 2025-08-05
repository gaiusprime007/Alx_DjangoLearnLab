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
from django.http import HttpResponse

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    # path('test/', views.test_view, name='test_view'),
    path('test/', lambda request: HttpResponse("Test URL is working!")),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
