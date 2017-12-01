# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote
import json
from django.views.decorators.csrf import csrf_exempt
import datetime


# Create your views here.

def get_dict_from_quote(quote):
	# print('hello world2')

	d = { "author": quote.author,
			"text": quote.text,
			"created": str(quote.created),
			"id": str(quote.id)	}

	return d

def get_quote_dicts(quotes):
	quotes_list = []
	for q in quotes:
		d = get_dict_from_quote(q)
		quotes_list.append(d)
	return quotes_list

def get_quotes_json(quotes):
	quotes_list = get_quote_dicts(quotes)

	json_quotes = json.dumps(quotes_list)
	return json_quotes

@csrf_exempt
def quotes(request):
	if request.method == 'GET':
		print(request.method)
		quotes = Quote.objects.all()

		json_quotes = get_quotes_json(quotes)
		
		return HttpResponse(json_quotes, content_type='application/json')


	if request.method == 'POST':
		print "PoSt request recieved"
		data = json.loads(request.body)

		created_dateTime = datetime.datetime.now()

		quote = Quote.objects.create(author = data["author"] , text = data["text"], created = created_dateTime)
		quote.save()

		new_quote = get_dict_from_quote(quote)

		new_quote = json.dumps(new_quote)



		return HttpResponse(new_quote, content_type='application/json')


# Get by ID functions
@csrf_exempt
def quote_by_id(request, quote_id):
	
	if request.method == 'GET':
		quotes = Quote.objects.get(id = quote_id)

		# print quote_id

		q = { "author": quotes.author,
				"text": quotes.text,
				"created": str(quotes.created)	}

		quote = json.dumps(q)

		return HttpResponse(quote, content_type = 'application/json')
	# return HttpResponse("get quote by id recieved")

	if request.method == 'POST':
		data = json.loads(request.body)

		print request.method
		print data

		return HttpResponse("PoSt quote by id recieved")

	if request.method == 'PATCH':

		data = json.loads(request.body)

		Quote.objects.filter(id=quote_id).update(**data)


		print request.method
		print data


		# return HttpResponse("PATCH quote by id recieved\n")
		quote = Quote.objects.get(id = quote_id)
		new_quote = get_dict_from_quote(quote)
		new_quote = json.dumps(new_quote)

		return HttpResponse(new_quote, content_type='application/json')

	if request.method == 'PUT':
		data = json.loads(request.body)

		print request.method
		print data

		return HttpResponse("PUT quote by id recieved\n")
