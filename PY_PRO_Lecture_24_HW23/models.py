from django.db import models
import uuid
import os

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position', )

class Dish(models.Model):

    # def get_file_name(self, file_name: str):
    #     ext = file_name.strip().split('.')[-1]
    #     file_name = f'{uuid.uuid4()}.{ext}'
    #     return os.path.join('dishes/%Y-%m-%d/', file_name)

    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    ingredients = models.CharField(max_length=255)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # photo = models.ImageField(upload_to=get_file_name, blank=True)
    photo = models.ImageField(upload_to='dishes/%Y-%m-%d', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('category', 'position')

    def __iter__(self):
        for item in self.dishes.all():
            yield item

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







