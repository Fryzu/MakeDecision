from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    _id = models.AutoField(primary_key=True)
    slug = models.SlugField(unique=True, max_length=140, blank=True, null=True)
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    content = models.TextField()

    class Meta:
        ordering = ['-update_date', '_id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'requested_slug': self.slug})

def create_slug(instance, *args, **kwargs):
    new_slug = slugify(instance.title)
    if Post.objects.filter(slug=new_slug).exists():
        new_slug = '%s-%s' %(new_slug, instance._id)
    if not instance.slug:
        instance.slug = new_slug
        instance.save()

post_save.connect(create_slug, sender=Post)
