from django.shortcuts import (render, render_to_response,
                              redirect, get_object_or_404)
from Wiki.forms import ArticleAddForm, ArticleEditForm, SearchForm
from Wiki.models import Article
import simplejson as json
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here

LOGIN_URL = 'auth/accounts/login/'


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
def wiki_view(request, slug):
    wiki = get_object_or_404(Article, slug=slug)
    return render(request, 'wiki_view.html', {'wiki': wiki})


# form to create a wiki"""
@login_required(login_url=LOGIN_URL)
def wiki_add_form(request):
    # instantiating a blank form
    article_form = ArticleAddForm
    return render(request, 'wiki_form.html', {'article_form': article_form})


# creating a wiki
@login_required(login_url=LOGIN_URL)
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
@login_required(login_url=LOGIN_URL)
def wiki_edit_form(request, slug=None):
    request.session['slug'] = slug
    wiki_slug = slug
    # get the wiki with its pk
    wiki = get_object_or_404(Article, slug=slug)
    # instantiate the form with an instance of the wiki to be edited
    article_edit_form = ArticleEditForm(instance=wiki)
    # then display the form
    return render(request, 'wiki_form.html',
                           {'article_edit_form': article_edit_form,
                            "slug": wiki_slug})


# Updating a wiki"""
@login_required(login_url=LOGIN_URL)
def wiki_update(request):
    slug = request.session['slug']
    wiki = get_object_or_404(Article, slug=slug)
    article_edit_form = ArticleEditForm(request.POST or None, instance=wiki)
    if request.method == 'POST':
        if article_edit_form.is_valid():
            wiki = article_edit_form.save(commit=False)
            article_edit_form.save()
            request.session['slug'] = None
            return redirect('/wikis/')
    return render(request, 'wiki_form.html',
                           {'article_edit_form': article_edit_form})


# deleting a wiki
@login_required(login_url=LOGIN_URL)
def wiki_delete(request, slug=None):
    """get the wiki"""
    wiki = get_object_or_404(Article, slug=slug)
    """delete the wiki"""
    wiki.delete()
    return redirect('/wikis/')
