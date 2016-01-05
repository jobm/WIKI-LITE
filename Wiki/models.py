from django.db import models
from autoslug import AutoSlugField
from django.utils.timezone import now
# Create your models here.


class Article(models.Model):
    title = models.CharField(blank=False, max_length=100)
    post = models.TextField(blank=False)
    category = models.CharField(blank=True, max_length=100, default='others')
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title')

    def __unicode__(self):
        return self.title
