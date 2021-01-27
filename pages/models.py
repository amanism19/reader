from django.db import models

# Create your models here.
class Book_Master(models.Model):
    book name = models.CharField(max_length=255,unique=True)
    alternate_name = models.CharField(max_length=255,unique=True)
    cover_image = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    synopsis = models.CharField(max_length=255)
    created_at = models.DateField()
    updated_at = models.DateField()
    deleted_at = models.DateField()
    user_id = models.IntegerField()
    date_of_publish = models.DateField()
    is_published = models.BooleanField()

    class Meta:
      db_table = "book_master"

class Book_attribute(models.Model):
    book_id = models.ForeignKey(Book_Master, on_delete=models.CASCADE)
    attribute_name = models.CharField(max_length=255)
    attribute_value = models.CharField(max_length=255)
    created_at = models.DateField()
    updated_at = models.DateField()
    deleted_at = models.DateField()
    user_id = models.IntegerField()

    class Meta:
      db_table = "book_attribute"

class Book_Chapter(models.Model):
    book_id = models.ForeignKey(Book_Master, on_delete=models.CASCADE)
    chapter_title = models.CharField(max_length=255) 
    chapter_sequence = models.IntegerField()
    author_note = models.CharField(max_length=255)
    chapter_content = models.TextField() 
    created_at = models.DateField()
    updated_at = models.DateField()
    deleted_at = models.DateField()
    user_id = models.IntegerField()
    date_of_publish = models.DateField()
    is_published = models.BooleanField()

    class Meta:
      db_table = "book_chapter"

class Book_Chapter_Feature(models.Model):
    book_id = models.ForeignKey(Book_Master, on_delete=models.CASCADE)
    chapter_id = models.ForeignKey(Book_Chapter, on_delete=models.CASCADE)
    chapter_attribute_name = models.CharField(max_length=255)
    chapter_attribute_value = models.CharField(max_length=255)
    created_at = models.DateField()
    updated_at = models.DateField()
    deleted_at = models.DateField()
    user_id = models.IntegerField()

    class Meta:
      db_table = "book_chapter_feature"

class Category_Master(models.Model):
    category_name = models.CharField(max_length=255)
    created_at = models.DateField()
    updated_at = models.DateField()
    deleted_at = models.DateField()
    user_id = models.IntegerField()

    class Meta:
      db_table = "category_master"

class Production_House_Master(models.Model):
    production_house_name = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    created_at = models.DateField()
    updated_at = models.DateField()
    deleted_at = models.DateField()
    user_id = models.IntegerField()

    class Meta:
      db_table = "production_house_master"


class Book_Category(models.Model):
    book_id = models.ForeignKey(Book_Master, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category_Master, on_delete=models.CASCADE)
    created_at = models.DateField()
    updated_at = models.DateField()
    deleted_at = models.DateField()
    user_id = models.IntegerField()

    class Meta:
      db_table = "book_category"


class Author_Master(models.Model):
    author_name = models.CharField(max_length=255)
    created_at = models.DateField()
    updated_at = models.DateField()
    deleted_at = models.DateField()
    user_id = models.IntegerField()

    class Meta:
      db_table = "author_master"

class Author_Production(models.Model):
    author_id= models.ForeignKey(Author_Master, on_delete=models.CASCADE)
    production_house_id = models.ForeignKey(Production_House_Master, on_delete=models.CASCADE)
    is_verified = models.BooleanField()
    created_at = models.DateField()
    updated_at = models.DateField()
    deleted_at = models.DateField()
    user_id = models.IntegerField()

    class Meta:
      db_table = "author_production"