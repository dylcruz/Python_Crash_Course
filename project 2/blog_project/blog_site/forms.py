from django import forms

from .models import Blog, BlogEntry

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name']
        labels = {'name': ''}

class BlogEntryForm(forms.ModelForm):
    class Meta:
        model = BlogEntry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
