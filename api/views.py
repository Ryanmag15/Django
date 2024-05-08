from django.http import JsonResponse
from .models import Aluno
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
import json



def index(request):
    alunos = Aluno.objects.all()
    alunos_json = serialize('json', alunos)
    return JsonResponse(alunos_json, safe=False)
   
@csrf_exempt
def editar_aluno(request, aluno_id):
    if request.method == 'PUT':
        try:
            aluno = Aluno.objects.get(id=aluno_id)
            
            # Analisa os dados do corpo da solicitação
            data = json.loads(request.body)
            
            # Atualiza os atributos do aluno com os valores recebidos
            for campo, valor in data.items():
                setattr(aluno, campo, valor)
                
            # Salva as alterações no banco de dados
            aluno.save()
            
            return JsonResponse({'status': 'ok'})
        except Aluno.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Aluno não encontrado'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)

@csrf_exempt
def excluir_aluno(request, aluno_id):
    if request.method == 'DELETE':  # Alterado para DELETE
        try:
            aluno = Aluno.objects.get(id=aluno_id)
            aluno.delete()
            return JsonResponse({'status': 'ok'})
        except Aluno.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Aluno não encontrado'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)

@csrf_exempt
def criar_aluno(request):
    if request.method == 'POST':
        dados_aluno = {}
        for campo, valor in request.POST.items():
            dados_aluno[campo] = valor
        aluno = Aluno(**dados_aluno)
        aluno.save()
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)
