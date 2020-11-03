from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

    id = models.AutoField('ID',primary_key=True)
    username = models.CharField(max_length = 25, unique=True)
    password = models.CharField(max_length = 300)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

class Trip(models.Model):

    id = models.AutoField('ID', primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    vehicle_model_id = models.IntegerField('Vehicle_ID', blank=False)
    package_id = models.IntegerField('Package_ID',null=True, blank=True, default=None)
    travel_type_id = models.IntegerField('Travel_Type_ID', blank=False, null=False)
    from_area_id = models.IntegerField('From_ID', blank=False, null=False)
    to_area_id   = models.IntegerField('To_ID', blank=True, null=True, default=None)
    from_city_id = models.IntegerField('From_City', blank=False, null=False)
    to_city_id = models.IntegerField('To_City', blank=True, null=True, default=None)
    from_date = models.DateTimeField('From_Date', blank=False)
    to_date  =  models.DateTimeField('To_Date', blank=True, null=True)
    online_booking = models.BooleanField('Online_Booking', default=False)
    mobile_site_booking = models.BooleanField('Mobile_Booking', default=False)
    from_lat = models.DecimalField('From_Lat', max_digits=9, decimal_places=6)
    from_long = models.DecimalField('From_Long', max_digits=9, decimal_places=6)
    to_lat = models.DecimalField('To_Lat', max_digits=9, decimal_places=6)
    to_long = models.DecimalField('To_Long', max_digits=9, decimal_places=6)
    car_cancellation = models.BooleanField('Car_Cancelled', default=False)

    def __str__(self):
        return str(self.id)

