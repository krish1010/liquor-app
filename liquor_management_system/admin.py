from django.contrib import admin

from .models import AadhaarInfo, State, Liquor, Transaction

admin.site.register(AadhaarInfo)
admin.site.register(State)
admin.site.register(Transaction)
admin.site.register(Liquor)
