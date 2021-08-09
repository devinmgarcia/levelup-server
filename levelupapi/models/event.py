from django.db import models
from django.db.models.fields import TimeField

class Event(models.Model):
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    description = models.TextField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    attendees = models.ManyToManyField("Gamer", through="GamerEvent", related_name="attending")

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value


