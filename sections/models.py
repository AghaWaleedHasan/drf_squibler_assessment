from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Create your models here.

class Section(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="section", null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    parent = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,related_name='children',default=None)
    slug = models.SlugField(unique=True,default=None)

    def __str__(self):
        return(self.title)

    def get_absolute_url(self):
        return reverse('sections', kwargs={'slug': self.slug})

@receiver(pre_save, sender=Section)
def store_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)