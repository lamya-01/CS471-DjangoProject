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

    
from django import forms
from .models import Student0, Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class Student0Form(forms.ModelForm):
    class Meta:
        model = Student0
        fields = '__all__'


from django import forms
from .models import Student2, Address2

class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = '__all__'

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = '__all__'


from .models import Book1
class Book1Form(forms.ModelForm):
    class Meta:
        model = Book1
        fields = '__all__'