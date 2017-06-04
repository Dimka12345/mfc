from django.contrib import admin
from mfc.models import Image, New, Passport, Service, Request, Document, PersonalInfo

admin.site.register([Image, New, Passport, Service, Request, Document, PersonalInfo])
