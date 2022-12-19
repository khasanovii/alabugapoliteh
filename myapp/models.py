from django.db import models

# Create your models here.
class People(models.Model):
    STATUS = (
        (1, 'first'),
        (2, 'second'),
        (3, 'third')
    )
    name = models.CharField(null=True, blank=True, max_length=50)
    surname = models.CharField(null=True, blank=True, max_length=50)
    age = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS, default=1)
    salary = models.IntegerField(default = 0)
    manager = models.CharField(null=True, blank=True, max_length=200)
    invite = models.CharField(null=True, blank=True, max_length=200)
