from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm
from .forms import EditarAlunoForm


def index(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/index.html', {'alunos': alunos})

def criar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = AlunoForm()
    return render(request, 'alunos/criar_aluno.html', {'form': form})

def editar_aluno(request, aluno_id):
    aluno = Aluno.objects.get(pk=aluno_id)
    if request.method == 'POST':
        form = EditarAlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditarAlunoForm(instance=aluno)
    return render(request, 'alunos/editar_aluno.html', {'form': form, 'aluno': aluno})

def excluir_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('index')
    return render(request, 'alunos/excluir_aluno.html', {'aluno': aluno})
