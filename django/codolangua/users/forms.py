from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите логин'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'А тут пароль -_-'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Повторите ваш пароль —__—'}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'placeholder': 'А сюда почту'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'placeholder': 'Как вас зовут?'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'placeholder': 'Как у вас фамилия?'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',

        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Такой email уже существует')
        return email