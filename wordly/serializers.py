from rest_framework import serializers
from .models import FiveLetterWord

class FiveLetterWordSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "word"
        )
        model = FiveLetterWord