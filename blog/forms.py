from django import forms

from .models import Post, Comment 

from ckeditor_uploader.fields import RichTextUploadingField

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)        