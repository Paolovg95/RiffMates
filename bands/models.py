from django.db import models

# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    def __str__(self):
        return f"Musician (id={self.id}, first_name={self.first_name}last_name={self.last_name})"
class Venue(models.Model):
    name = models.CharField(max_length=20)

class Room(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=20)
