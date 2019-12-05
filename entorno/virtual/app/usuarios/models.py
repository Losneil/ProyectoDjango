from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from parametros.models import TipoDocu, EstaCivil, Etnia, TipoEstu, TipoLogr, Empleos
# Create your models here.

class Usuarios(models.Model):
    IdUsuario = models.CharField(max_length=50, verbose_name="Numero de Identificacion", default="")
    IdTipDoc = models.ForeignKey(TipoDocu, default="", on_delete=models.CASCADE, verbose_name="Tipo documento")
    IdEstCiv = models.ForeignKey(EstaCivil, default="", on_delete=models.CASCADE, verbose_name="Estado Civil")
    IdEtnias = models.ForeignKey(Etnia, default="", on_delete=models.CASCADE, verbose_name="Etnias")
    ImagUsua = models.ImageField(verbose_name="Foto de Perfil", upload_to="perfiles/img")
    PerfilPro = RichTextField(default="Candidato...", verbose_name="Perfil Profesional")
    GeneUsua = models.CharField(max_length=1, default="O", verbose_name="Genero")
    TeleUsua = models.CharField(max_length=20, default="0", verbose_name="Telefono")
    CeluUsua = models.CharField(max_length=20, default="0", verbose_name="Celular")
    DireUsua = models.TextField(default="0", verbose_name="Direccion Postal")
    RegiUsua = models.DateTimeField(default=0, auto_now_add=False, verbose_name="Registrado el:")
    EstaUsua = models.CharField(max_length=50, default="Activo", verbose_name="Estado")

    class Meta:
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"

    def __str__(self):
        return self.IdUsuario

class Experiencia(models.Model):
    CargExpe = models.ForeignKey(Empleos, on_delete = models.CASCADE, limit_choices_to = {'Escargo': 'SI'}, verbose_name = "Cargo Ocupado")
    EmprExpe = models.CharField(max_length=150, verbose_name="Empresa")
    TeleEmpr = models.CharField(max_length=30, verbose_name="Contacto de la empresa")
    JefeExpe = models.CharField(max_length=30, verbose_name="Perosonal de la empresa")
    FechInic = models.DateTimeField(auto_now_add=False, default=0, verbose_name="Fecha de Inicio")
    FechaFin = models.DateTimeField(auto_now_add=False, default=0, verbose_name="Fecha de Terminacion")
    FuncionE = RichTextField(verbose_name="Funciones Desempeñadas")
    LogrExpe = RichTextField(verbose_name="Logros Alcanzados")
    SopoExpe = models.FileField(upload_to="soportes/laboral", default="", verbose_name="Certificado Laboral")
    ExtaExpt = models.CharField(max_length=30, default="Activo", verbose_name="Estado de Experiencia")

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencia Laboral"

    def __str__(self):
        return self.CargExpe

class Educacion(models.Model):
    TipoEstu = models.ForeignKey(TipoEstu, on_delete=models.CASCADE, default="", verbose_name="Tipo de Educacion")
    Instituto = models.CharField(max_length=30, default="Activo", verbose_name="Academia")
    TituloEst = models.CharField(max_length=250, verbose_name="Titulo Obtenido")
    FechGrado = models.DateTimeField(auto_now_add=False, default=0, verbose_name="Fecha de Graduacion")
    SoporteEs = models.FileField(upload_to="soportes/educacion", default="", verbose_name="Soporte Educacion")
    EstaEstu = models.CharField(max_length=30, default="Activo", verbose_name="Estado de Educacion")

    class Meta:
        verbose_name = "Educacion"
        verbose_name_plural = "Estudios Registrados"

    def __str__(self):
        return self.TituloEst

class Logros(models.Model):
    NombTiLo = models.ForeignKey(TipoLogr, on_delete=models.CASCADE, verbose_name="Tipo de Logro")
    FechLogr = models.DateTimeField(auto_now_add=False, default=0, verbose_name="Fecha de Culminacion")
    NombLogr = models.CharField(max_length=100, default="Activo", verbose_name="Logro o Distincion")
    DescLogr = RichTextField(verbose_name="Descripcion del Logro")

    class Meta:
        verbose_name = "Logros"
        verbose_name_plural = "Logros Obtenidos"

    def __str__(self):
        return self.NombLogr

class Habilidades(models.Model):
    NombHabil = models.CharField(max_length=100, default="Activo", verbose_name="Habilidad")
    NiveHabil = models.CharField(max_length=20, default="Activo", verbose_name="Nivel de Habilidad:")

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return self.NombHabil