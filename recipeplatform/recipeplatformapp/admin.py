from django.contrib import admin
from .models import Recipe

# Register your models here.
class recipeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Recipe,recipeAdmin)

