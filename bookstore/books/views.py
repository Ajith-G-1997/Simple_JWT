from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from books.models import User
from books.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied



class RegisterUser(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            refresh = RefreshToken.for_user(customer)
            return Response({"message": "User created."}) 
        else:
            return Response(serializer.errors)





class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        book = self.get_object()
        if book.author != request.user:
            raise PermissionDenied("You do not have permission to update this book.")
        return super().put(request, *args, **kwargs)


class BookDeleteAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        if book.author != request.user:
            raise PermissionDenied("You do not have permission to delete this book.")
        return super().delete(request, *args, **kwargs)

