from django import forms
from django.core.exceptions import ValidationError

from .models import Comment


class CommentForm(forms.ModelForm):
    # author = forms.CharField(required=True, widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'your name'
    # }))
    comment = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'your comment',
        'id': 'contact_comment'
    }))

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        return comment

    def clean(self):
        data = self.cleaned_data
        author = data.get('author')
        comment = data.get('comment')
        if comment == 'valid':
            raise ValidationError('Wrong comment!')
        print(data)
        return data

    class Meta:
        model = Comment
        fields = ('author', 'comment')
