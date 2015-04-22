from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Inventory(models.Model):
    items = models.CommaSeparatedIntegerField(max_length=30)

    def __str__(self):
        return self.items


class Character(models.Model):
    # By default Django uses the primery key of the related object.
    # Hence, no need to specify User.id.
    user_id = models.OneToOneField(User, limit_choices_to={'is_admin': False},
                                   blank=True)
    name = models.CharField(max_length=100)
    inventory = models.ForeignKey(Inventory)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100, default="Item")
    damage = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    consumable = models.BooleanField(default=False)

    def __str__(self):
        return self.name
