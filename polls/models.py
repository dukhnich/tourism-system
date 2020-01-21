from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.conf import settings

class Sight(models.Model):
    name_sight = models.CharField(max_length=60)
    description = models.TextField()
    img = models.ImageField(upload_to='photo_sight')
    year = models.IntegerField()
    address = models.CharField(max_length=100)
    link = models.URLField()
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("sight", kwargs = {
        'slug': self.slug
        })

TYPE_CHOICES = (
    ('VIP', 'VIP'),
    ('Lite', 'Lite')
)

class Type(models.Model):
    #type - lite or VIP
    type = models.CharField(choices=TYPE_CHOICES, max_length=4)
    days = models.IntegerField()
    desc = models.TextField()
    price = models.FloatField()
    type_slug = models.SlugField()
    def get_absolute_url(self):
        return reverse("ticket", kwargs = {
        'pk': self.id
        })

class Item(models.Model):
    #type_ticket - store all fields about type
    type_ticket = models.ForeignKey(Type,on_delete=models.CASCADE)
    name_person = models.CharField(max_length=20)
    surname_person = models.CharField(max_length=20)
    date_start = models.DateField()
    #def create(cls, type_ticket, name_person, surname_person, date_start):
        #item = cls(type_ticket = type_ticket, name_person = name_person, surname_person = surname_person, date_start= date_start )
        # do something with the item
        #return item
