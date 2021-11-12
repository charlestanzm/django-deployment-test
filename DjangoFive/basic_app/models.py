from django.db import models

# import the basic User model from the django framework 
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model): 

    # Relate this model to the default User model, 
        # do NOT inherit the User class directly, may screw up the databse
    user = models.OneToOneField(User, on_delete=models.CASCADE) 

    # additional fields to be added to the model 
    portfolio_site = models.URLField(blank = True) # blank = T means it's an optional field
    # requires pillow 
    profile_pic = models.ImageField(upload_to = 'profile_pic', blank = True) 

    def __str__(self): 
        return self.user.username 


# REMEMBER TO REGISTER YOUR MODEL IN ADMIN.PY! #