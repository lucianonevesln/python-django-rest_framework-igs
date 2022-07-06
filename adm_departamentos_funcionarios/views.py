from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AdmDepartamentosSerializer, AdmFuncionariosSerializer
from .models import Departamentos, Funcionarios

### Endpoint que será apresentado ao iniciar a aplicação ###

@api_view(['GET'])
def AdmDepartamentosFuncionariosOverview(request):
    api_urls = {
        'Listar Departamentos': '/departamentos-listar/',
        'Detalhes de Departamento': '/departamento-detalhes/<str:pk>/',
        'Criar Departamento': '/departamento-cadastrar/',
        'Editar Departamento': '/departamento-editar/<str:pk>/',
        'Excluir Departamento': '/departamento-excluir/<str:pk>/',
        'Listar Funcionários': '/funcionarios-listar/',
        'Detalhes de Funcionário': '/funcionario-detalhes/<str:pk>/',
        'Inserir Funcionário': '/funcionario-cadastrar/',
        'Editar Funcionário': '/funcionario-editar/<str:pk>/',
        'Excluir Funcionário': '/funcionario-excluir/<str:pk>/',
    }
    return Response(api_urls)

## CRUD Departamentos ##

# Endpoint que lista departamentos
@api_view(['GET'])
def AdmDepartamentosListar(request):
    departamentos = Departamentos.objects.all()
    serializer = AdmDepartamentosSerializer(departamentos, many=True)
    return Response(serializer.data)

# Endpoint que mostra detalhes por departamento
@api_view(['GET'])
def AdmDepartamentosDetalhes(request, pk):
    departamentos = Departamentos.objects.get(id=pk)
    serializer = AdmDepartamentosSerializer(departamentos, many=False)
    return Response(serializer.data)

# Endpoint que cadastra departamento
@api_view(['POST'])
def AdmDepartamentosCadastrar(request):
    serializer = AdmDepartamentosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Endpoint que edita departamento
@api_view(['PUT'])
def AdmDepartamentosEditar(request, pk):
    departamento = Departamentos.objects.get(id=pk)
    serializer = AdmDepartamentosSerializer(instance=departamento, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Endpoint que exclui departamento
@api_view(['DELETE'])
def AdmDepartamentosExcluir(request, pk):
    departamento = Departamentos.objects.get(id=pk)
    departamento.delete()
    return Response('Departamento deletado com sucesso!')

## CRUD Funcionários ##

# Endpoint que lista funcionários
@api_view(['GET'])
def AdmFuncionariosListar(request):
    funcionarios = Funcionarios.objects.all()
    serializer = AdmFuncionariosSerializer(funcionarios, many=True)
    return Response(serializer.data)

# Endpoint que mostra detalhes por funcionário
@api_view(['GET'])
def AdmFuncionariosDetalhes(request, pk):
    funcionario = Funcionarios.objects.get(id=pk)
    serializer = AdmFuncionariosSerializer(funcionario, many=False)
    return Response(serializer.data)

# Endpoint que cadastra funcionário
@api_view(['POST'])
def AdmFuncionariosCadastrar(request):
    serializer = AdmFuncionariosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Endpoint que edita funcionário
@api_view(['PUT'])
def AdmFuncionariosEditar(request, pk):
    funcionario = Funcionarios.objects.get(id=pk)
    serializer = AdmFuncionariosSerializer(instance=funcionario, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Endpoint que exclui funcionário
@api_view(['DELETE'])
def AdmFuncionariosExcluir(request, pk):
    funcionario = Funcionarios.objects.get(id=pk)
    funcionario.delete()
    return Response('Funcionario deletado com sucesso!')