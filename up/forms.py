from django import forms
from .models import it
#DataFlair #File_Upload
class tofill_Form(forms.ModelForm):
    class Meta:
        model = it
        fields = [
        'fil'
        ]