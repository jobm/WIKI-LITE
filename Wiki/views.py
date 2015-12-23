from django.shortcuts import render
from Wiki.forms import ArticleForm
# Create your views here.
def home(request):
    return render(request,'home.html')

def wiki(request):
    article_form = ArticleForm
    return render(request,'wiki_home.html',context={'article_form': article_form})