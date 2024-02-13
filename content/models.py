from django.db import models
from bands.models import Musician, Band
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class SeekingChoice(models.TextChoices):
    MUSICIAN = "M"
    BAND = "B"

class SeekingAd(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.SET_NULL, blank=True, null=True)
    # on_delete=models.SET_NULL means if the owner of an existing object got deleted set this field for existing object to null.
    band = models.ForeignKey(Band, on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # a CharField using the choices argument so seeking can only contain "M" or "B" indicating whether a musician or band is being sought
    seeking = models.CharField(max_length=1, choices=SeekingChoice.choices)
    content = models.TextField()
    # auto_now=True means this field gets automatically populated with the current date when the object gets created
    date = models.DateTimeField(auto_now=True)
    content = models.TextField()



    def clean(self):
        if self.seeking == SeekingChoice.MUSICIAN:
            # When seeking a musician, ensure the band field gets populated and the musician field is empty
            if self.band is None:
                raise ValidationError("Band is mandatory when seeking a musican")
            if self.musician is not None:
                raise ValidationError("Musician field should be empty wehn seeking one")
        else:
            if self.musician is None:
                raise ValidationError("Musician field is mandatory when seeking a band")
            if self.band is not None:
                raise ValidationError("Band field should be empty when seeking one")
        super().clean()


# When seeking a band, ensure the musician field gets populated and the band field is empty
