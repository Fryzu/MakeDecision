from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    slug = models.SlugField(unique=True, max_length=140, blank=True, null=True)
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    content = models.TextField()

    def __str__(self):
        return self.title

    def _create_slug(self):
        new_slug = slugify(self.title)
        if Post.objects.filter(slug=new_slug).exists():
            new_slug = '%s-%s' %(new_slug, self.id)
        return new_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._create_slug()
        super().save(*args, **kwargs)

    #TODO add post detail view using django.urls.reverse() 
    # https://docs.djangoproject.com/pl/2.1/ref/urlresolvers/
    def get_absolute_url(self):
        pass
