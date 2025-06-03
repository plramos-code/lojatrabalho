from django.forms import ModelForm
from .models import Produto

class ProdutoForm(ModelForm):
    class Meta: # armazena metadados
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'estoque']