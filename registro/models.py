from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Expediente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=255, verbose_name="Codigo expediente")
    COMERCIAL = 'COMERCIAL'
    LABORAL = 'LABORAL'
    PENAL = 'PENAL'
    CIVIL = 'CIVIL'
    ADMINISTRATIVO = 'ADMINISTRATIVO'
    CONSTITUCIONAL = 'CONSTITUCIONAL'

    TIPO_PROCESO = (
        (COMERCIAL, 'Comercial'),
        (LABORAL, 'Laboral'),
        (PENAL, 'Penal'),
        (CIVIL, 'Civil'),
        (ADMINISTRATIVO, 'Administrativo'),
        (CONSTITUCIONAL, 'Constitucional')
    )
    tipo = models.CharField(max_length=50, verbose_name="Tipo Expediente", choices=TIPO_PROCESO, default=LABORAL)
    descripcion = models.TextField(verbose_name="Descripcion", default="modificar")
    numero_folio = models.SmallIntegerField(verbose_name="Numero de folios", default=0)
    estado = models.BooleanField(verbose_name="Estado", blank=True, null=True)
    flag = models.BooleanField(verbose_name="Revision", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")


    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
        ordering = ['codigo', 'created', 'updated']


    def __str__(self):
        return self.codigo