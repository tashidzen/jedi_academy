from django import forms
from .models import Candidate, Jedi

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ("name",)
        #exclude = ('jedi', 'question',)

class DjedayForm(forms.ModelForm):
    class Meta:
        model = Jedi
        #fields =("")  # поля, которые необходимо включить
        exclude = ('',)  # поля, которые необходимо исключить(не отображать)

class UserForm(forms.Form):
    name = forms.CharField(label="Имя", min_length=1)
    planet = forms.CharField(label="Планета", min_length=1)
    age = forms.IntegerField(label="Ваш возраст", min_value=1)
    email = forms.CharField(min_length=1)

