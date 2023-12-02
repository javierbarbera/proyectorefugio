from django import forms

class LibroFormulario(forms.Form):
    titulo= forms.CharField(max_length=50)
    autor= forms.CharField(max_length=50)
    sinopsis= forms.CharField(widget=forms.Textarea)

class DiscoFormulario(forms.Form):
    titulo= forms.CharField(max_length=50)
    interprete= forms.CharField(max_length=50)

class PeliculaFormulario(forms.Form):
    titulo= forms.CharField(max_length=50)
    director= forms.CharField(max_length=50)
    sinopsis= forms.CharField(widget=forms.Textarea)