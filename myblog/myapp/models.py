from django.db import models
from django.utils.timezone import now

# Create your models here.
# pip install Pillow
class Post(models.Model):
    title = models.CharField(max_length=255)
    post_body = models.TextField()
    image = models.ImageField(upload_to='photo', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Myfriend(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=200)
    address = models.TextField()
    email = models.EmailField()
    photo = models.ImageField(upload_to='photo')
    created = models.DateField()

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    post_body = models.TextField()
    image = models.ImageField(upload_to='photo', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

