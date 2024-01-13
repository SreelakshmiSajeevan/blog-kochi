from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100, default="")
    title= models.CharField(max_length=100, default="")
    id = models.AutoField(primary_key=True)
    short_description= models.CharField(max_length=200, default="")
    content= RichTextField()
    thumbnail=models.ImageField(upload_to="blog_images")
    created_at = models.TimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
