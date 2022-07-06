#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Departamentos(models.Model):
    nome_departamento = models.CharField(max_length=30)

    def __str__(self):
            return 'Departamento: {}'.format(self.nome_departamento)


class Funcionarios(models.Model):
    id_departamento = models.ForeignKey(Departamentos, models.DO_NOTHING,\
                                        db_column='id_departamento')
    nome_funcionario = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
            return 'Número do Departamento: {},\
                    Nome do Funcionário: {},\
                    E-mail: {},\
                    Salário: {}'.\
                format(self.id_departamento,\
                       self.nome_funcionario,\
                       self.email, self.salario)
