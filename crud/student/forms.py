from .models import Student
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'Name':forms.TextInput(attrs={'class':'form-control','autocomplete':'off','placeholder':'Enter Name'}),
            'Email':forms.TextInput(attrs={'class':'form-control','autocomplete':'off','placeholder':'Enter Email'}),
            'City':forms.TextInput(attrs={'class':'form-control','autocomplete':'off','placeholder':'Enter City'}),
            'Gender':forms.TextInput(attrs={'class':'form-control','autocomplete':'off','placeholder':'Enter Gender'}),
            'Phone':forms.TextInput(attrs={'class':'form-control','autocomplete':'off','placeholder':'Enter Phone'})
        }
        