from django.db import models

import uuid

# Create your models here.
from django.contrib.auth.models import User



class Order(models.Model):

	id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False ) 
	
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True, auto_now=False)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)
     



def __str__(self):
		return str(self.id)
	
  






class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name



class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
