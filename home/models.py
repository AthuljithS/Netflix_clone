from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    genre=models.CharField(max_length=100)
    image=models.CharField(max_length=2500)
    rating=models.FloatField(default=0.0)
    year=models.IntegerField(default=2026)

    def __str__(self):
        return self.title