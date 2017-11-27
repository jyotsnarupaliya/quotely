# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote
import json

# Create your views here.

def get_dict_from_quote(quote):
	print('hello world2')

	d = { "author": quote.author,
			"text": quote.text,
			"created": str(quote.created)	}

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

def quotes(request):
	print(request.method)
	quotes = Quote.objects.all()

	json_quotes = get_quotes_json(quotes)
	
	return HttpResponse(json_quotes, content_type='application/json')
