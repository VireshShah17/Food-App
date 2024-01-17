from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length = 200)
    item_desc = models.CharField(max_length = 200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length = 500, default = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRmjivXii4HjtyuaSeTbuZxX23TPkv701da9FplhGeyg&s")


    def __str__(self) -> str:
        return self.item_name
