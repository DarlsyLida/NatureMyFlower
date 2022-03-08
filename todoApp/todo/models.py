from django.db import models
from django.utils import timezone
from matplotlib.pyplot import cla

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # date_created = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Stories(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Counsellors(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Cases(models.Model):
    location = models.CharField(max_length=100)
    description = models.TextField()
    state = models.CharField(max_length=20)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Officers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name