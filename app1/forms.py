from django import forms

class StudentForm(forms.Form):
    name=forms.CharField(max_length=50)
    roll=forms.IntegerField()
    summary=forms.CharField(max_length=500)