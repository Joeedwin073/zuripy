from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





# Title : A string of maxlength 200, use Django’s models.CharField

 

# Text : Any amount of text, use Django’s TextField

 

# Author : A Foreign Key to the current user model. Make use of Django’s get_user_model function.

 

# Created_date : A date-time column, use Django’s models.DateTimeField. 

 

# Published_date : A date-time column, use Django’s models.DateTimeField. 

 