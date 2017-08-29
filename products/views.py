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
	if department == 'men':
		department_results = Product.objects.all().filter(department="MEN'S")
	elif department == 'women':
		department_results = Product.objects.all().filter(department="WOMEN'S")
	else:
		department_results = Product.objects.all()

	# get sort by query parameter
	sort_by = request.GET.get('sortby')
	if sort_by == "lowtohigh":
		most_discounted = department_results.order_by('current_price')
	elif sort_by == "hightolow":
		most_discounted = department_results.order_by('-current_price')
	else:
		most_discounted = department_results.order_by('-markdown')

	paginator = Paginator(most_discounted, 40)
	# get page query parameter
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
		'products' : products,
		'department' : department
	}
	return HttpResponse(template.render(context, request))