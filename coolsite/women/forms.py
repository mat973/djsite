from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'is_published', 'photo', 'cat']
        widgets = {
            'titel': forms.TextInput(attrs={'class': 'form-input'}),
            'content:': forms.Textarea(attrs={'cols': 60, 'row': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина привышает 200 символов')
        return title
# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     slug = forms.SlugField(max_length=255,label='URL')
#     content = forms.CharField(widget= forms.Textarea(attrs={'cols':60, 'row':10}), label='Информация')
#     is_published = forms.BooleanField(label='Публикация', required=False, initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(),label='Категории', empty_label='категория не выбрана')