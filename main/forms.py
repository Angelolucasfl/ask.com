from django.forms import ModelForm
from . models import Pergunta

class PerguntaForm(ModelForm):
    class Meta:
        model = Pergunta
        fields = '__all__'
        exclude = ['host']