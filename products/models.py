# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=50)
	brand = models.CharField(max_length=50)
	department = models.CharField(max_length=50)
	current_price = models.DecimalField(max_digits=7, decimal_places=2)
	original_price = models.DecimalField(max_digits=7, decimal_places=2)
	markdown = models.DecimalField(max_digits=4, decimal_places=2)
	image = models.CharField(max_length=200)
	link = models.CharField(max_length=200)