from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter the Title',
                'max_length': 15,
            }
        ),
    )
    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter the Content',
            }
        ),
        error_messages={
            'required': 'Please input data',
        }
    )

    class Meta:
        model = Article
        fields = '__all__'