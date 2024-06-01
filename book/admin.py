from django.contrib import admin
from . models import Book , Review , Author
# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name' , 'age' , 'birth_date']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title' , 'author' , 'price' , 'publish_date']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book' , 'reviewer_name' , 'review' , 'rate']
    

