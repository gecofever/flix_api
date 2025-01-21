from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[MinValueValidator(0, 'Nota não pode ser inferior a Zero.'),
                    MaxValueValidator(5, 'Nota não pode ser superior a Cinco.')]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.movie)