from rest_framework import serializers
from adm_departamentos_funcionarios import models


class AdmDepartamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Departamentos
        fields = '__all__'


class AdmFuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Funcionarios
        fields = '__all__'