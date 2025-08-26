from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name