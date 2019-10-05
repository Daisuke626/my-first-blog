from django.db import models
class Person(models.Model):
    last_name = models.CharField(max_length = 20)
    first_name = models.CharField(max_length = 20)
    pass
# Create your models here.
