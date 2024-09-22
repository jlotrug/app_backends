from django.db import models
from django.core.validators import MinLengthValidator


class FiveLetterWord(models.Model):
    word = models.CharField(max_length=5, validators=[MinLengthValidator(5)], null=False, blank=False)
    # active = models.BooleanField(default=False)

    def __str__(self):
        return self.word