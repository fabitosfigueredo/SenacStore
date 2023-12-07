from django import forms
from StoreApp.models import Cliente

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length = 100)
    email = forms.EmailField()
    telefone = forms.CharField(required=False)
    assunto = forms.CharField(max_length = 100)
    mensagem = forms.CharField(widget=forms.Textarea)

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
