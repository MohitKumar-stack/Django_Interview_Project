from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import databse
# Register your models here.
# admin.site.register(databse)
@admin.register(databse)
class Databse(admin.ModelAdmin):
    list_display=['id','UserName','Email','Password']