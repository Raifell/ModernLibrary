from django.contrib import admin
from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'rating')


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Genre)
