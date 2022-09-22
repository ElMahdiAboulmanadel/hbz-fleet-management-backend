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
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.email

# Models for the HBZ TMS API

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name="driver")
    driving_license = models.FileField(upload_to = user_directory_path, blank=True, null=True)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=255)
    vehicle_number = models.CharField(max_length=255)
    vehicle_model = models.CharField(max_length=255)
    vehicle_capacity_quantity = models.IntegerField()
    vehicle_capacity_unit = models.CharField(max_length=255, choices=user_constants.VEHICLE_CAPACITY_UNIT_CHOICES)
    vehicule_mileage = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.vehicle_number

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name="client")
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    company_city = models.CharField(max_length=255)
    company_phone_number = models.CharField(max_length=255)
    company_email = models.CharField(max_length=255)
    company_website = models.CharField(max_length=255, blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class Merchandise(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="merchandise")
    weight_quantity = models.IntegerField()
    weight_unit = models.CharField(max_length=255, choices=user_constants.WEIGHT_UNIT_CHOICES)
    volume_quantity = models.IntegerField()
    volume_unit = models.CharField(max_length=255, choices=user_constants.VOLUME_UNIT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Container(models.Model):
    container_number = models.CharField(max_length=255)
    container_type = models.CharField(max_length=255)
    container_capacity_quantity = models.IntegerField()
    container_capacity_unit = models.CharField(max_length=255, choices=user_constants.VEHICLE_CAPACITY_UNIT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.container_number

class Trip(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="trip")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="trip")
    container = models.ForeignKey(Container, on_delete=models.CASCADE, related_name="trip")
    merchandises = models.ManyToManyField(Merchandise, related_name="trip")
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    distance = models.IntegerField()
    status = models.CharField(max_length=255)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    consumption = models.IntegerField()
    driver_price = models.IntegerField()
    client_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.origin + " -> " + self.destination

class Vidange(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="vidange")
    date = models.DateTimeField()
    mileage = models.IntegerField()
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.vehicle.vehicle_number + " " + self.date

class Panne(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="panne")
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="panne")
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="panne")
    mileage = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.vehicle.vehicle_number

class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="maintenance")
    date = models.DateTimeField()
    mileage = models.IntegerField()
    pannes = models.ManyToManyField(Panne, related_name="maintenance")
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.vehicle.vehicle_number + " " + self.date

class Entretien(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="entretien")
    date = models.DateTimeField()
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.vehicle.vehicle_number + " " + self.date