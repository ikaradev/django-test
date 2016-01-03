# coding: utf-8

from django.contrib import admin
from cms.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "publisher", "page")
    list_display_links = ("id", "name")
admin.site.register(Book, BookAdmin)


