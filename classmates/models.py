from django.db import models

# Create your models here.

class Classmate(models.Model):

    Male = 'M'
    Female = 'F'
    GENDER_CHOICES = (
    (Male, 'Male'),
    (Female, 'Female'),
    )

    firstname = models.CharField(max_length=200, blank = False, null = False)
    lastname = models.CharField(max_length=200, blank = False, null = False)
    age = models.IntegerField(blank = False, null = False)
    address = models.CharField(max_length=200, blank = False, null = False)
    gender = models.CharField(max_length=200, choices = GENDER_CHOICES, default = Male)


    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse('classmate_edit', kwargs={'pk': self.pk})
