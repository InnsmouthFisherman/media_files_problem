from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, \
                                      DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, \
                                       PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic.base import TemplateResponseMixin, View
from django.forms.models import modelform_factory
from django.apps import apps
from django.core.exceptions import ImproperlyConfigured
from braces.views import CsrfExemptMixin, JsonRequestResponseMixin
from .models import Article
from .forms import ArticleForm

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'content/detail.html',
        {'article': article})

def list(request):
  return render(request, 'content/list.html', {
    'articles': Article.objects.all()
  })

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = ArticleForm()
    return render(request, 'content/create.html', {'form': form})
