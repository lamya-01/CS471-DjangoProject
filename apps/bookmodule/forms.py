from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']

        title = forms.CharField(
           max_length=100,
           required=True,
           label="Title",
           widget=forms.TextInput(attrs={
              'placeholder': 'Enter book title',
              'class': 'mycssclass',
               'id': 'jsID'
             })
        )
        author = forms.CharField(
            max_length=100,
            required=True,
            label="Author",
            widget=forms.TextInput(attrs={
              'placeholder': 'Enter author name',
              'class': 'mycssclass'
            })
        )
        price = forms.DecimalField(
            required=True,
            label="Price",
            initial=0
        )

        edition = forms.IntegerField(
            required=True,
            initial=1,
            widget=forms.NumberInput()
        )

    
