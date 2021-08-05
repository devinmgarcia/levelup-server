from django.db import models
from django.db.models.fields import TimeField

class Event(models.Model):
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    description = models.TextField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    date = models.DateField()
    time = TimeField()

