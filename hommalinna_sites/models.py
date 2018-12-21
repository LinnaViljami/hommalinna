# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
import json


class VisitorMessage(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank='true')
    def __str__(self):
        return self.title

class Location(models.Model):
    token = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(default=datetime.now, blank='true')
    def __str__(self):
        return self.name
