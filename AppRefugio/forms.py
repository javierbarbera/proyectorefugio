from django import forms
from django.contrib.auth.forms import UserCreationForm, UserModel, UserChangeForm
from django.contrib.auth.models import User
from AppRefugio.models import Libro

class LibroFormulario(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'subtitulo','autor','fecha', 'sinopsis', 'imagen', 'autor_entrada']

class DiscoFormulario(forms.Form):
    titulo= forms.CharField(max_length=50)
    interprete= forms.CharField(max_length=50)

class PeliculaFormulario(forms.Form):
    titulo= forms.CharField(max_length=50)
    director= forms.CharField(max_length=50)
    sinopsis= forms.CharField(widget=forms.Textarea)

# class UserCreationFormCustom(UserCreationForm):
#     user = forms.TextInput(label="Usuario")
#     email = forms.EmailField()
#     password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
#     password1 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

#     class Meta:
#         model = UserModel
#         fields = ["username", "email", "password1", "password2"] 
#         help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su mail: ")
    last_name = forms.CharField(label="Apellido: ")
    first_name = forms.CharField(label="Nombre: ")
    imagen = forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = User
        fields = ["email", "last_name", "first_name", "imagen"]

