from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['matricula', 'nome', 'email', 'telefone', 'data_nascimento', 'data_ingresso']
        
class EditarAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['matricula', 'nome', 'email', 'telefone', 'data_nascimento', 'data_ingresso']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Obtém a instância do aluno a ser editado
        aluno_instance = kwargs.get('instance')
        if aluno_instance:
            # Preenche os campos do formulário com os valores do aluno
            self.fields['matricula'].initial = aluno_instance.matricula
            self.fields['nome'].initial = aluno_instance.nome
            self.fields['email'].initial = aluno_instance.email
            self.fields['telefone'].initial = aluno_instance.telefone
            self.fields['data_nascimento'].initial = aluno_instance.data_nascimento
            self.fields['data_ingresso'].initial = aluno_instance.data_ingresso
        