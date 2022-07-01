from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# this model is created to connect profile with User and add new fields
class Profile( models.Model ):
    # OneToOneField is using to connect our Profile model with User
    # on_delet = CASCADE is used to delete Profile model when user is deleted
    user = models.OneToOneField( User, on_delete =models.CASCADE )
    image = models.ImageField( default = 'profilepic.jpg', upload_to = 'profile_picture' )
    location = models.CharField( max_length = 100 )

    def __str__(self):
        return self.user.username