from django.shortcuts import (render, render_to_response,
                              redirect, get_object_or_404)
from Wiki.forms import ArticleAddForm, ArticleEditForm, SearchForm
from Wiki.models import Article
from haystack.query import SearchQuerySet
import json
from django.http import HttpResponse
# Create your views here


# this is the view for registered users
def wikis(request):
    return render(request, 'wiki_home.html')


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
    # get the wiki with its pk
    wiki = get_object_or_404(Article, id=pk)
    # instantiate the form with an instance of the wiki to be edited
    article_edit_form = ArticleEditForm(instance=wiki)
    # then display the form
    return render(request, 'wiki_form.html',
                           {'article_edit_form': article_edit_form})


# Updating a wiki"""
def wiki_update(request):
    wiki = get_object_or_404(Article, pk=request.session.get('id'))
    article_edit_form = ArticleEditForm(request.POST or None, instance=wiki)
    if request.method == 'POST':
        if article_edit_form.is_valid():
            article_edit_form.save()
            return redirect('/wikis/')
    return render(request, 'wiki_form.html',
                           {'article_edit_form': article_edit_form})


# deleting a wiki
def wiki_delete(request):
    """get the wiki"""
    wiki = get_object_or_404(Article, pk=request.session.get('id'))
    """delete the wiki"""
    wiki.delete()
    request.session['id'] = None
    return redirect('/wikis/')


# haystack search"""
def search_titles(request):
    ct_auto = SearchQuerySet().filter(auto_title=request.GET.get('q', ''))
    data = json.dumps({
        'results': [article.title for article in ct_auto]
    })
    return HttpResponse(data, content_type='application/json')
