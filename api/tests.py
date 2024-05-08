from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Aluno

class AlunoAPITestCase(APITestCase):
    def setUp(self):
        self.aluno = Aluno.objects.create(email='test@example.com', nome='Ryan Teste', matricula='123456', telefone='1234567890', data_nascimento='1990-01-01', data_ingresso='2022-01-01')

    def test_aluno_list(self):
        url = reverse('aluno-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_aluno_detail(self):
        url = reverse('aluno-detail', kwargs={'pk': self.aluno.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
