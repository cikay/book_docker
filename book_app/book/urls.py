from django.urls import path

from .view import BookView, AuthorView

urlpatterns = [
    path('author/', AuthorView.as_view()),
    path('book/', BookView.as_view()),
]