from django.shortcuts import (render, render_to_response,
                              redirect, get_object_or_404)
from Wiki.forms import ArticleAddForm, ArticleEditForm, SearchForm
from Wiki.models import Article, ArticleFilter
from haystack.query import SearchQuerySet
import simplejson as json
from django.http import HttpResponse
from django.db.models import Q
# Create your views here


# this is the view for registered users
def wikis(request):
    wikis = Article.objects.all()
    categories = Article.objects.all()
    query = request.GET.get('q')

    if query:
        wikis = wikis.filter(Q(category__icontains=query)).distinct()
    context = {"wikis": wikis, 'categories': categories}
    return render(request, 'wiki_home.html', context=context)


# view a single Wiki
def wiki_view(request, pk):
    wiki = get_object_or_404(Article, pk=pk)
    return render(request, 'wiki_view.html', {'wiki': wiki})


# form to create a wiki"""
def wiki_add_form(request):
    # instantiating a blank form
    article_form = ArticleAddForm
    return render(request, 'wiki_form.html', {'article_form': article_form})


# creating a wiki
def wiki_create(request):
    # instantiating the form with a POST request if one exists"""
    article_form = ArticleAddForm(request.POST or None)
    # checking the request method"""
    if request.method == 'POST':
        # checking whether the form is valid"""
        if article_form.is_valid():
            # saving the form"""
            article_form.save()
            # redirecting to the page with wikis"""
            return redirect('/wikis')
    # Srendering the form again if its invalid"""
    return render(request, 'wiki_form.html', {'article_form': article_form})


# editing and article"""
def wiki_edit_form(request, pk):
    request.session['id'] = pk
    wiki_pk = pk
    # get the wiki with its pk
    wiki = get_object_or_404(Article, id=pk)
    # instantiate the form with an instance of the wiki to be edited
    article_edit_form = ArticleEditForm(instance=wiki)
    # then display the form
    return render(request, 'wiki_form.html',
                           {'article_edit_form': article_edit_form,
                            "id": wiki_pk})


# Updating a wiki"""
def wiki_update(request, pk=None):
    wiki = get_object_or_404(Article, pk=pk)
    article_edit_form = ArticleEditForm(request.POST or None, instance=wiki)
    if request.method == 'POST':
        if article_edit_form.is_valid():
            article_edit_form.save()
            return redirect('/wikis/')
    return render(request, 'wiki_form.html',
                           {'article_edit_form': article_edit_form})


# deleting a wiki
def wiki_delete(request, pk=None):
    """get the wiki"""
    wiki = get_object_or_404(Article, pk=pk)
    """delete the wiki"""
    wiki.delete()
    return redirect('/wikis/wiki/')


# haystack search
def search_titles(request):
    ct_auto = SearchQuerySet().autocomplete(auto_title=
                                            request.GET.get('q', ''))[:5]
    data = json.dumps({
        'results': [article.title for article in ct_auto]
    })
    return HttpResponse(data, content_type='application/json')
