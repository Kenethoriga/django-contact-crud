from django.db import models

# Create your models here.


from django.db import models
from django.utils import timezone 


class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    upload_date = models.DateTimeField(default=timezone.now)


