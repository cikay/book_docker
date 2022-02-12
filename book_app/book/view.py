
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Book, Author
from .serializer import BookSerializer, AuthorSerializer


class AuthorView(APIView):

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class BookView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
