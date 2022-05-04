from django import forms
from django.forms import formset_factory, ModelForm
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'image','file']
