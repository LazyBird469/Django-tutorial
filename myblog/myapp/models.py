from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    post_body = models.TextField()

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

