# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Product


# Create your views here.
def index(request):
	most_discounted_products = Product.objects.order_by('-markdown')[:100]
	template = loader.get_template('products/index.html')
	context = {
		'most_discounted' : most_discounted_products
	}
	return HttpResponse(template.render(context, request))