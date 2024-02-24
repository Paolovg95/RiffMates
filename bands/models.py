from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)
    picture = models.ImageField(blank=True, null=True)

    # profile_picture = models.ImageField(blank=True, null=True)
    def __str__(self):
        return f"Musician (id={self.id}, first_name={self.first_name}, last_name={self.last_name})"

class Band(models.Model):
    name = models.CharField(max_length=100)
    musicians = models.ManyToManyField(Musician)
    def __str__(self):
        return f"Band={self.id}, Name={self.name}"

# def user_path(instance, filename):
#     return f"user{instance.owner.id}/{filename}"
class Venue(models.Model):
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"Venue={self.id}, Name={self.name}"

class Room(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=20)

    def __str__(self):
        return f"Room={self.id}, Name={self.room_name},Venue={self.venue.name}"

class UserProfile(models.Model):
    # Create a one-to-one relationship between the UserProfile and the User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    musician_profiles = models.ManyToManyField(Musician, blank=True)
    venue_profiles = models.ManyToManyField(Venue, blank=True)
    # relationships between this user account and any Musician or Venue objects.
