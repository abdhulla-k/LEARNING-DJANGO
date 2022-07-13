from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Item( models.Model ):
    def __str__(self):
        return self.item_name

    user_name = models.ForeignKey( User, on_delete = models.CASCADE, default = 1 )
    item_name = models.CharField( max_length = 200 )
    itm_desc = models.CharField( max_length = 200 )
    itm_price = models.IntegerField()
    item_image = models.CharField(
        max_length = 500, 
        default= 'https://www.dirtyapronrecipes.com/wp-content/uploads/2015/10/food-placeholder.png'
    )

    def get_absolute_url( self ):
        return reverse( "food:detail", kwargs = { "pk": self.pk })