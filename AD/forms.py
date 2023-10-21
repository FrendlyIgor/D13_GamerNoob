from django.forms import ModelForm, Textarea
from .models import AD, Comment
from django import forms

# Создаём модельную форму
class ADForm(ModelForm):
  class Meta:
    model = AD
    fields = ['author', 'title', 'categoryType', 'text',]
    widgets = {
           
      'title' : forms.TextInput(attrs={
      'placeholder' : 'Напиши название',
      'class': 'form-control'
      }),
      'text' : forms.Textarea(attrs={
      'class': 'form-control',
      'placeholder' : 'Напиши текст'
      })
    }

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['text',]
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for field in self.fields:
        self.fields[field].widget.attrs['class'] = 'form-control'
      self.fields['text'].widget = Textarea(attrs={'rows':3})