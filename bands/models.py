from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    def __str__(self):
        return f"Musician (id={self.id}, first_name={self.first_name}, last_name={self.last_name})"

class Band(models.Model):
    name = models.CharField(max_length=100)
    musicians = models.ManyToManyField(Musician)
    def __str__(self):
        return f"Band={self.id}, Name={self.name}"

class Venue(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"Venue={self.id}, Name={self.name}"

class Room(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=20)

    def __str__(self):
        return f"Room={self.id}, Name={self.room_name},Venue={self.venue.name}"
