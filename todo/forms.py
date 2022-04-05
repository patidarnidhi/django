from django import forms
from todo.models import Todo
from todo.models import Contact


class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields={"title","description","name"}

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields={"name","lname","email","phone"}

