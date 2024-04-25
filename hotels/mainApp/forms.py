from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields=['username','email','password1','password2']

class ReservationForm(forms.Form):
    check_in_date = forms.DateField(label='Дата заезда')
    check_out_date = forms.DateField(label='Дата выезда')
    guest_count = forms.IntegerField(label='Количество гостей')