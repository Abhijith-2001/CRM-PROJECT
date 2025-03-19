from django.contrib import admin

# Register your models here.

from .models import PaymentStructure

admin.site.register(PaymentStructure)