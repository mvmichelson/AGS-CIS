#Programa PYTHON
#Aplicacion: AGS CIS/AUDIT
#Definicion de Formularios de la Aplicacion
#Programado por Marco A. Villalobos M.
#============================================

from django.contrib.auth.models import User, Group
#from django.contrib.admin.widgets import AutocompleteSelect
#from django.contrib.admin import widgets
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from django.core.exceptions import ValidationError
#from django.forms import ValidationError

# from django.utils.translation import ugettext_lazy as _
# Se debe cambiar ugettext_lazy  por version django 4.xx 
from django.utils.translation import gettext_lazy as _
import datetime #for checking renewal date range.

from .models import Obj_Ries_Mod, Modulo_Mod, Framework, Parametros_G, Gestor, Tipo_OC, Auditorias


#************************************************************************************************************************
#***************************************        1. FrameWorks   ***********************************************************
#************************************************************************************************************************


class Crea_FrameForm(forms.Form):
    """
    Creacion de un Framewor
    """

    #codigo  = forms.CharField(max_length=10, widget=forms.Textarea(attrs={'rows':1, 'cols':10}))
    nombre  = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'rows':1, 'cols':200}))
    version = forms.CharField(max_length=10, widget=forms.Textarea(attrs={'rows':1, 'cols':10}))
    descripcion  = forms.CharField(max_length=400, widget=forms.Textarea(attrs={'rows':2, 'cols':200}))
    institucion  = forms.CharField(max_length=150, widget=forms.Textarea(attrs={'rows':1, 'cols':150})) 

    #descripcion  = forms.CharField(max_length=400)
    #institucion  = forms.CharField(max_length=150)


    # Validaciones

    #def clean_nombre(self):
        
        #nombre=self.cleaned_data['nombre']
        #existe = Drp.objects.filter(nombre=nombre)

        #if existe:
        #    raise ValidationError(_('*** Nombre de DRP ya existe ***'))
            
        #return nombre 

class Crea_ModuloForm(forms.Form):
    """
    Creacion de Modulo
    """
    item=forms.CharField(max_length=20, widget=forms.Textarea(attrs={'rows':1, 'cols':20}))
    nombre=forms.CharField(max_length=100, widget=forms.Textarea(attrs={'rows':1, 'cols':100}))

class Crea_OCForm(forms.Form):
    """
    Creacion de Objetivo de Control
    """
    item=forms.CharField(max_length=20, widget=forms.Textarea(attrs={'rows':1, 'cols':20}))
    nombre=forms.CharField(max_length=100, widget=forms.Textarea(attrs={'rows':1, 'cols':100}))
    descripcion=forms.CharField(max_length=600, widget=forms.Textarea(attrs={'rows':3, 'cols':200}))


#************************************************************************************************************************
#***************************************        1. Auditorias   ***********************************************************
#************************************************************************************************************************

class Crea_AuditoriaForm(forms.Form):
    """
    Creacion de Auditoria
    """

    codigo=forms.CharField(max_length=20, widget=forms.Textarea(attrs={'rows':1, 'cols':20}))
    nombre=forms.CharField(max_length=100, widget=forms.Textarea(attrs={'rows':1, 'cols':100}))
    objetivo=forms.CharField(max_length=600, widget=forms.Textarea(attrs={'rows':3, 'cols':200}))
    fecha_ini=forms.DateTimeField(widget=forms.DateInput(attrs={"type": "date"}))
    fecha_ter=forms.DateTimeField(widget=forms.DateInput(attrs={"type": "date"}))
    auditor_sup=forms.ModelChoiceField(queryset=Gestor.objects.all())
    auditor_ejec=forms.ModelChoiceField(queryset=Gestor.objects.all())
    framework=forms.ModelChoiceField(queryset=Framework.objects.all(), empty_label='Sin Framework', required=False)

    #Verifica que el codigo de la Auditoria no haya sido asignado
    def clean_codigo(self):
        
        codigo=self.cleaned_data['codigo']
        existe = Auditorias.objects.filter(cod_aud=codigo)

        if existe:
            raise ValidationError(_('El Codigo ya ha sido asignado a otra Auditoria'))
            
        return codigo 
    
    def clean_fecha_ter(self):

        fecha_i=self.cleaned_data['fecha_ini']
        fecha_t=self.cleaned_data['fecha_ter']
        
        if fecha_t < fecha_i:
            raise ValidationError(_('La Fecha de termino es anterior a la fecha de inicio'))
        
        return fecha_t



class FileForm(forms.Form):
    """
    Elige Planilla Excel con Auditoria para Importar 
    """
    ruta = forms.FileField(label='Selecciona un archivo')
