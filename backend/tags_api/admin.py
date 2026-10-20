from django.contrib import admin

from .models import Tag

@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name',)
