from django.shortcuts import (render)
from haystack.query import SearchQuerySet


# views
def home_page(request):
    return render(request, 'home.html')


# haystack search
def search_titles(request):
    ct_auto = SearchQuerySet().autocomplete(
        auto_title=request.GET.get('q', ''))[:5]
    data = json.dumps({
        'results': [article.title for article in ct_auto]
    })
    return HttpResponse(data, content_type='application/json')
