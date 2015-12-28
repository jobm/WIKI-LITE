from haystack import indexes
from Wiki.models import Article
from django.utils import timezone

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)


    #for autocomplete
    content_auto = indexes.EdgeNgramField(model_attr='slug')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()