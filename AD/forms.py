from django.forms import ModelForm
from .models import AD
from django import forms

# Создаём модельную форму
class ADForm(ModelForm):
# В класс мета, как обычно, надо написать модель, по которой будет строиться форма, и нужные нам поля. Мы уже делали что-то похожее с фильтрами
   class Meta:
       model = AD
       fields = ['author', 'title', 'categoryType', 'text',]
       widgets = {
           """ 'author' : forms.TextInput(attrs={
               'placeholder' : 'Напиши Имя',
               'class': 'form-control'
           }), """
           'title' : forms.TextInput(attrs={
           'placeholder' : 'Напиши название',
           'class': 'form-control'
         }),
         'text' : forms.Textarea(attrs={
           'class': 'form-control',
           'placeholder' : 'Напиши текст'
         })
       }