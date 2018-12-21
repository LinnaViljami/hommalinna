# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import VisitorMessage, Location

admin.site.register(VisitorMessage)
admin.site.register(Location)
