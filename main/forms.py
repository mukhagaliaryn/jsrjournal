from django import forms
from main.models import Article, Review


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
