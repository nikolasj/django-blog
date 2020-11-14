from django import forms
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

    class Meta:
        model = Comment
        fields = ('author', 'comment')
