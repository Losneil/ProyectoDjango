from django.db import models

# Create your models here.

# Estado civil
class EstaCivil(models.Model):
    NombEsci = models.CharField(max_length = 50, verbose_name = "Estado Civil")

    class Meta:
        verbose_name = "Estado Civil"
        verbose_name_plural = "Estados Civiles"

    def __str__(self):
        return self.NombEsci

# Grupo etnico
class Etnia(models.Model):
    NombEtni = models.CharField(max_length = 50, verbose_name = "Grupo Etnico")

    class Meta:
        verbose_name = "Grupo Etnico"
        verbose_name_plural = "Grupos Etnicos"

    def __str__(self):
        return self.NombEtni

# Tipo de documento
class TipoDocu(models.Model):
    NombTipo = models.CharField(max_length = 50, verbose_name = "Tipo de Documento")

    class Meta:
        verbose_name = "Tipo de Documento"
        verbose_name_plural = "Tipos de Documentos"

    def __str__(self):
        return self.NombTipo

# Tipo de estudiante
class TipoEstu(models.Model):
    NombTiEs = models.CharField(max_length = 50, verbose_name = "Tipo de Estudiante")

    class Meta:
        verbose_name = "Tipo de Estudiante"
        verbose_name_plural = "Tipos de Estudiantes"

    def __str__(self):
        return self.NombTiEs

# Tipo de logro
class TipoLogr(models.Model):
    NombTiLo = models.CharField(max_length = 50, verbose_name = "Tipo de Logro")

    class Meta:
        verbose_name = "Tipo de Logro"
        verbose_name_plural = "Tipos de Logros"

    def __str__(self):
        return self.NombTiLo

# Esto es opcional
class Empleos(models.Model):
    NombEmpl = models.CharField(max_length = 50, verbose_name = "Tipo de Empleo")

    class Meta:
        verbose_name = "Tipo de Empleo"
        verbose_name_plural = "Tipos de Empleos"

    def __str__(self):
        return self.NombEmpl
