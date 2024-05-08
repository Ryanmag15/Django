from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('editar/<int:aluno_id>/', views.editar_aluno, name='editar_aluno'),
    path('excluir/<int:aluno_id>/', views.excluir_aluno, name='excluir_aluno'),
    path('criar/', views.criar_aluno, name='criar_aluno'),
]
