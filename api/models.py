from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from api.managers import UserManager
from . import constants as user_constants

def user_directory_path(instance, filename):
        return 'uploads/driving_licences/user_{0}/{1}'.format(instance.user.id, filename)

class User(AbstractUser):
    username = None # remove username field, we will use email as unique identifier
    email = models.EmailField(unique=True, null=True, db_index=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.PositiveSmallIntegerField(choices=user_constants.USER_TYPE_CHOICES)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserManager()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name="user_profile")
    phone_number = models.CharField(max_length=255,blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    city = models.CharField(max_length=255,blank=True,null=True)
    driving_license = models.FileField(upload_to = user_directory_path, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.email
