# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Product


# Create your views here.
def listings(request, department=None):
	# get department parameter
	if department == 'M':
		department_results = Product.objects.all().filter(department="MEN'S")
	elif department == 'W':
			department_results = Product.objects.all().filter(department="WOMEN'S")
	else:
		department_results = Product.objects.all()

	most_discounted = department_results.order_by('-markdown')
	paginator = Paginator(most_discounted, 40)
	# get page parameter
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page
		products = paginator.page(1)
	except EmptyPage:
		# If page is out of range, deliver last page of results
		products = paginator.page(paginator.num_pages)
	
	template = loader.get_template('products/index.html')
	context = {
		'products' : products
	}
	return HttpResponse(template.render(context, request))