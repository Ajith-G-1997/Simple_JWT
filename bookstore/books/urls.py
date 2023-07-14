from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterUser,BookListAPIView, BookDetailAPIView, BookCreateAPIView, BookUpdateAPIView, BookDeleteAPIView



urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    
   
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('books/create/', BookCreateAPIView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateAPIView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteAPIView.as_view(), name='book-delete'),
]
