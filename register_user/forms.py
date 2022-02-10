from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from django.contrib.auth.models import User



class UserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Nome")
    last_name = forms.CharField(label="Sobrenome")
    password1 = forms.CharField(label='password',
                                help_text='Sua senha precisa conter pelo menos 8\
                                        caracteres e não pode ser inteiramente\
                                        numérica', 
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme o password', 
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
        )
        help_texts = {
            'username': None,
        }
        

class UserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'readonly': 'readonly'})
        }
        help_texts = {
            'username': "Não é possivel Editar o UserName",
        }