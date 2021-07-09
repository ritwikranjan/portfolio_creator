from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=200)
    level = models.PositiveSmallIntegerField()

class PersonalDetail(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    github = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    dob = models.DateField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if PersonalDetail.objects.count() > 0:
            pass
        else:
            super(PersonalDetail, self).save(*args, **kwargs)


