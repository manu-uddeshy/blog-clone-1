from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.models import model_to_dict
from blog.models import Post , Comment

class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable meduim-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable meduim-editor-textarea'})
        }