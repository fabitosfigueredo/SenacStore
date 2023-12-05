from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length = 100)
    email = forms.EmailField()
    telefone = forms.CharField()
    assunto = forms.CharField(max_length = 100)
    mensagem = forms.CharField(widget=forms.Textarea)