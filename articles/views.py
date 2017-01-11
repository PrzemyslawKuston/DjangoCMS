from django.shortcuts import render_to_response, render, redirect
from articles.models import Article, Comment
from .forms import CommentForm
from django.utils import timezone #do automatycznej daty publikacji
from django.http import HttpResponseRedirect

# Create your views here.

def articles(request):
    return render_to_response('articles.html', { 'articles' : Article.objects.all() })

def article(request, article_id):
    return render_to_response('article.html', { 'article': Article.objects.get(id=article_id) })

def add_comment(request,article_id):
	art = Article.objects.get(id=article_id)
	if request.method == "POST":  # formularz
		cf = CommentForm(request.POST)
		if cf.is_valid():
			comment = cf.save(commit=False)
			comment.published = timezone.now()
			comment.article = art
			comment.save()

			return HttpResponseRedirect('/articles/%s' % article_id)

	else:
		cf = CommentForm()

	args = {}
	args['article'] = art
	args['form'] = cf

	return render(request,'add_comment.html', args)
