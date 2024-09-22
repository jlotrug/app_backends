from django.urls import path
from .views import FiveLetterWordList

urlpatterns = [
    path('fiveletter-words/', FiveLetterWordList.as_view(), name="fiveletter_words"),
]