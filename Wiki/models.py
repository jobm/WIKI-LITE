from django.db import models

# Create your models here.


class Shared(models.Model):
    title = models.CharField(blank=False, max_length=100)
    post = models.TextField(blank=False)
    views = models.IntegerField(blank=True, default=0)
    category = models.CharField(blank=True, max_length=100, default='others')
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True


class Article(Shared):
    slug = models.SlugField(unique=True)
    created = models.BooleanField(default=False)

    @models.permalink
    def get_absolute_url(self):
        return 'wiki: article', (self.slug,)


class Draft(Shared):
    created = models.BooleanField(default=False)