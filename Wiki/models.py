from django.db import models
from autoslug import AutoSlugField
from django.utils.timezone import now
# Create your models here.


class Shared(models.Model):
    title = models.CharField(blank=False, max_length=100)
    post = models.TextField(blank=False)
    category = models.CharField(blank=True, max_length=100, default='others')
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True


class Article(Shared):
    slug = AutoSlugField(populate_from='title')
    created = models.BooleanField(blank=True, default=False)

    # @models.permalink
    # def get_absolute_url(self):
    #     return 'wiki: article', (self.slug,)



class Draft(Shared):
    created = models.BooleanField(blank=True, default=False)