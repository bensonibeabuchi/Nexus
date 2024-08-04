from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Product)
admin.site.register(Tag)
# admin.site.register(Profile)


class OrderAdmin(admin.ModelAdmin):
    list_display = ["product", "customer", "status",]
    list_editable = ["status"]


admin.site.register(Order, OrderAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "email", 'address']


admin.site.register(Customer, CustomerAdmin)
