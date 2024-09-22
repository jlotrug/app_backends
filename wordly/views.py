from django.shortcuts import render
from rest_framework import generics
from .serializers import FiveLetterWordSerializer
from .models import FiveLetterWord

class FiveLetterWordList(generics.ListCreateAPIView):
    queryset = FiveLetterWord.objects.all()
    serializer_class = FiveLetterWordSerializer
