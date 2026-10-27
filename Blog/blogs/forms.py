from django import forms

from .models import Blog, Post


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['title']
        labels = {'title': 'Blog Title'}


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text']

        widgets = {
            'text': forms.Textarea(
                attrs={'cols': 80}
            )
        }