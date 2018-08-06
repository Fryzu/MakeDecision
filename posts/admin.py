from django.contrib import admin
from .models import *

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "id"]
    exclude=['slug']
    readonly_fields=['slug']
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
