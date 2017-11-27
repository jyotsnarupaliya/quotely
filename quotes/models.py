# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Quote(models.Model):
	author = models.CharField(max_length = 200)
	created = models.DateTimeField()
	text = models.CharField(max_length = 500)