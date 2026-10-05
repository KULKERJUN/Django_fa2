from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=100, null=True)

class BlogModel(models.Model):
    categ = [
        ('Education','Education' ),
        ('Technologies','Technologies'),
        ('Sports','Sports')
    ]
    title = models.CharField(max_length=200,null=True)
    author_name = models.CharField(max_length=100, null=True)
    content = models.TextField()
    category = models.CharField(choices=categ, max_length=100,null=True)
    blog_image = models.ImageField(upload_to='media/projectimg',null=True)
    publish_date = models.DateField(auto_now_add= True, null=True)


