from django.contrib import admin

# Register your models here.

from .models import Author,Book
 
# Register your models here.
 
 
admin.site.register(Author)
admin.site.register(Book)
