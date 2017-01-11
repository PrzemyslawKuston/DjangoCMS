from django import forms
from models import Comment

#formularze edycji komentarza
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','content')
