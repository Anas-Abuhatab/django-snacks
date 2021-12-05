from django.contrib import admin
from .models import Things
# Register your models here.

@admin.register(Things)
class AdminThings(admin.ModelAdmin):
    list_display = ['title', 'description']