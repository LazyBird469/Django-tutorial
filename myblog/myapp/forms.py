from django import forms
from.models import *

class PostCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post_body', 'image']

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'post_body', 'image']

# class BlogUpdateForm1(forms.ModelForm):
#     class Meta:
#         model = Blog
#         fields = ['title',  'photo1']