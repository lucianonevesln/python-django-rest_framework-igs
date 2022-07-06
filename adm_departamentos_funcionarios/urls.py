from django.urls import path
from . import views

urlpatterns = [
    # cadastro de url de apresentação geral
    path('', views.AdmDepartamentosFuncionariosOverview, name='adm-departamentos-funcionarios'),

    # cadastros de urls de crud de departamentos
    path('departamentos-listar/', views.AdmDepartamentosListar, name='departamentos-listar'),
    path('departamento-detalhes/<str:pk>/', views.AdmDepartamentosDetalhes, name='departamento-detalhes'),
    path('departamento-cadastrar/', views.AdmDepartamentosCadastrar, name='departamento-cadastrar'),
    path('departamento-editar/<str:pk>/', views.AdmDepartamentosEditar, name='departamento-editar'),
    path('departamento-excluir/<str:pk>/', views.AdmDepartamentosExcluir, name='departamento-excluir'),

    # cadastros de urls de crud de funcionários
    path('funcionarios-listar/', views.AdmFuncionariosListar, name='funcionarios-listar'),
    path('funcionario-detalhes/<str:pk>/', views.AdmFuncionariosDetalhes, name='funcionario-detalhes'),
    path('funcionario-cadastrar/', views.AdmFuncionariosCadastrar, name='funcionario-cadastrar'),
    path('funcionario-editar/<str:pk>/', views.AdmFuncionariosEditar, name='funcionario-editar'),
    path('funcionario-excluir/<str:pk>/', views.AdmFuncionariosExcluir, name='funcionario-excluir'),
]