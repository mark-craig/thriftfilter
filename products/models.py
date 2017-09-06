# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=100)
	brand = models.CharField(max_length=100)
	department = models.CharField(max_length=50)
	current_price = models.DecimalField(max_digits=7, decimal_places=2)
	original_price = models.DecimalField(max_digits=7, decimal_places=2)
	markdown = models.DecimalField(max_digits=4, decimal_places=2)
	image = models.CharField(max_length=500)
	link = models.CharField(max_length=500)
	# timestamp fields
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)