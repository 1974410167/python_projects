from django import forms
from .models import Student

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class Student_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','address']


class practice_form(forms.Form):
    grade = forms.IntegerField(label='your grade')
    teacher = forms.CharField(label='your teacher',max_length=100)

