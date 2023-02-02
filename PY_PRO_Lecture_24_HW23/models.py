from django.db import models

class About(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='about/')

class Who_us(models.Model):
    title = models.CharField(max_length=20)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    desc = models.TextField(max_length=100)
    photo = models.ImageField(upload_to='who_us/', unique=True)

class Menu(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    ingredients = models.CharField(max_length=255)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='menu/%Y-%m-%d', blank=True)
    is_special = models.BooleanField(default=False)

class Specials(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    ingredients = models.CharField(max_length=255)
    desc = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='specials/%Y-%m-%d')
    is_special = models.BooleanField(default=False)

class Events(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='events/%Y-%m-%d')







