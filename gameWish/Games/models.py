from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    genre = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    developer = models.CharField(max_length=200)
    release_date = models.DateField()

    def __str__(self):
        return self.name