from django import forms

class DateForm(forms.Form):
    start_Date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    end_Date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))