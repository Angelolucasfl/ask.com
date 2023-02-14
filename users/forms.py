from django.forms import ModelForm
from . models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'nome_usuario', 'bio']