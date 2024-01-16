from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Doctor(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE)
#     image = models.ImageField(upload_to='patient/images/')
#     mobile_no = models.CharField(max_length = 12)
    
#     def __str__(self):
#         return f"{self.user.first_name} {self.user.last_name}"

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(null=True, blank=True,upload_to='accounts/images/')
    mobile_no = models.CharField(max_length = 12)
    is_patient = models.BooleanField(default = False)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"