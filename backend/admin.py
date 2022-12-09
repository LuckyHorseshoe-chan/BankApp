from django.contrib import admin
from .models import User, Currency, Country, Bank, Check, Operation, Active

admin.site.register(User)
admin.site.register(Currency)
admin.site.register(Country)
admin.site.register(Bank)
admin.site.register(Check)
admin.site.register(Operation)
admin.site.register(Active)