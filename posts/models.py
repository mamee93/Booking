from django.db import models
from  django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
     
    user    = models.ForeignKey(User,related_name='userpost', on_delete=models.CASCADE)
    title   = models.CharField(max_length=100)
    image   = models.ImageField(upload_to='post/')
    content = models.TextField(blank=True, null=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    category = models.ForeignKey('Category',related_name='post_category', on_delete=models.CASCADE,limit_choices_to={'main_category':True},blank=True, null=True)
    post_slug   = models.SlugField(blank=True, null=True)
    tags = models.CharField(max_length=50)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.post_slug = self.title
        super(Post,self).save(*args, **kwargs)
        

class Category(models.Model):
    name = models.CharField(max_length=50)
    main_category = models.ForeignKey('self',limit_choices_to={'main_category':None},related_name='maincategory', on_delete=models.CASCADE, blank=True, null=True)
    image = models.CharField(max_length=50)
    def __str__(self):
        return self.name
