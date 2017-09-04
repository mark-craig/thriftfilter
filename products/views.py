# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import FieldError

from .models import Product

from datetime import datetime, timedelta


# Create your views here.
def listings(request, department=None):
	men_dep, wom_dep, all_dep = False, False, False
	# get department parameter
	if department == 'men':
		results = Product.objects.all().filter(department="MEN'S")
		men_dep = True
	elif department == 'women':
		results = Product.objects.all().filter(department="WOMEN'S")
		wom_dep = True
	else:
		results = Product.objects.all()
		all_dep = True

	# only show products which have been updated within the last 30 hours
	start_date = datetime.now() - timedelta(hours=30)
	end_date = datetime.now()
	results = results.filter(updated_at__range=[start_date, end_date])

	# get search query
	query = request.GET.get('query')
	jumbotron_msg = "Today's Best Deals"
	if query is not None:
		jumbotron_msg = 'Showing product results for "' + query +'"'
		try:
			# this command relies on a postgresql database with the pg_trgm extension
			results = results.filter(name__unaccent__lower__trigram_similar=query)
		except FieldError:
			# if another database is being used, such as sqllite, just do a simple 'contains' filter 
			results = results.filter(name__contains=query)
			jumbotron_msg += '\t(exact matches)'


	# get sort by query parameter
	sort_by = request.GET.get('sortby')
	sort_msg = 'Sorting by largest discount'
	if sort_by == "lowtohigh":
		results = results.order_by('current_price')
		sort_msg = 'Sorting by lowest price'
	elif sort_by == "hightolow":
		results = results.order_by('-current_price')
		sort_msg = 'Sorting by highest price'
	else:
		results = results.order_by('-markdown')

	paginator = Paginator(results, 40)
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
		'men_dep' : men_dep,
		'wom_dep' : wom_dep,
		'all_dep' : all_dep,
		'sort_msg' : sort_msg,
		'jumbotron_msg' : jumbotron_msg
	}
	return HttpResponse(template.render(context, request))