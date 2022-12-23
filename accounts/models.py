from sre_constants import CATEGORY
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)

class Ticket(models.Model):
    STATUS=(
        ('Open','Open'),
        ('Pending', 'Pending'),
        ('InProgess','InProgess'),
        ('Resolved','Resolved'),
    )
    CATEGORY=(
        ('Type1','Type1'),
        ('Type2','Type2'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null = True, choices=STATUS, default='Open')
    comment = models.CharField(max_length=200, null = True)
    def __str__(self):
        return str(self.title)