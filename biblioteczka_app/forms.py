from django import forms
from django.core.exceptions import ValidationError

from biblioteczka_app.models import Author

def check_year(value):
    if value < -5000:
        raise ValidationError("NIe było kisązek w tym czasie")

class AddBookForm(forms.Form):
    title = forms.CharField()
    year = forms.IntegerField(validators=[check_year])
    author = forms.ModelChoiceField(queryset=Author.objects.all())