from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     title = models.CharField(max_length=100)
     content = CKEditor5Field('Text', config_name='extends')
     date = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.title

class Comments(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     comment = models.TextField(max_length=300)
     author = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

     def __str__(self):
          return self.comment