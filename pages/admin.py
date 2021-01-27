from django.contrib import admin
from models import *
# Register your models here.

class AdminBook_Master(admin.ModelAdmin):
    model = Book_Master
    list_display = Book_Master._meta.get_fields()

class AdminBook_attribute(admin.ModelAdmin):
    model = Book_attribute
    list_display = Book_attribute._meta.get_fields()

class AdminBook_Chapter(admin.ModelAdmin):
    model = Book_Chapter
    list_display = Book_Chapter._meta.get_fields()

class AdminBook_Chapter_Feature(admin.ModelAdmin):
    model = Book_Chapter_Feature
    list_display = Book_Chapter_Feature._meta.get_fields()

class AdminCategory_Master(admin.ModelAdmin):
    model = Category_Master
    list_display = Category_Master._meta.get_fields()

class AdminProduction_House_Master(admin.ModelAdmin):
    model = Production_House_Master
    list_display = Production_House_Master._meta.get_fields()

class AdminBook_Category(admin.ModelAdmin):
    model = Book_Category
    list_display = Book_Category._meta.get_fields()

class AdminAuthor_Master(admin.ModelAdmin):
    model = Author_Master
    list_display = Author_Master._meta.get_fields()

class Adminauthor_production(admin.ModelAdmin):
    model = Author_Production
    list_display = Author_Production._meta.get_fields()


admin.site.register( Book_Master, AdminBook_Master, Book_attribute, AdminBook_attribute, Book_Chapter, AdminBook_Chapter, Book_Chapter_Feature, AdminBook_Chapter_Feature, Category_Master, AdminCategory_Master, Production_House_Master, AdminProduction_House_Master, Book_Category, AdminBook_Category, Author_Master, AdminAuthor_Master, Author_Production, AdminAuthor_Production)