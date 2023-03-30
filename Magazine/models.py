from django.db import models

# Create your models here.

class Article(models.Model):
    
    full_desc = models.TextField()
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=100)
    image = models.ImageField(upload_to ='pics')
   # article_id = models.IntegerField(default=1)


        
        
