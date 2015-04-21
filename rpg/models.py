from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Invetory(models.Model):
    id = models.AutoField(primary_key=True)
    items = models.CommaSeparatedIntegerField(max_length=30)

    def __str__(self):
        return self.items


class Character(models.Model):
    # By default Django uses the primery key of the related object.
    # Hence, no need to specify User.id.
    user_id = models.OneToOneField(User, primary_key=True,
                                   limit_choices_to={'is_admin': False})
    char_name = models.CharField(max_length=100)
    inventory = models.ForeignKey(Invetory)

    def __str__(self):
        return self.char_name


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100, default="Item")
    damage = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    consumable = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name
