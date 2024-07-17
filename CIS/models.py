#Modelo de Datos Modelo CIS del Sistema AGS

from django.db import models

from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User, Group
from datetime import date

#====================================
# ENTIDADES o MODELOS
#====================================

#ENTIDADES DEL USUARIO
#ENTIDADES DEL FRAMEWORK
#ENTIDADES DE LA AUDITORIA


#-----------------------------------
#--- ENTIDADES DEL USUARIO   -------
#-----------------------------------

class Gestor(models.Model):
    """
    Entidad: Gestor
            Registra los atributos de un gestor del Sistema
    """

    user_pk = models.IntegerField(null=True)
    user_gestor = models.OneToOneField(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    #user_grupos = models.ManyToManyField(Group) No se puede hacer esta definicion!!
    
    cargo = models.CharField(max_length= 50, blank=True)
    apellido= models.CharField(max_length= 50, blank=True)
    #area =  models.ForeignKey('Area', on_delete=models.SET_NULL, null=True)
    fono_t = models.CharField(max_length= 50, blank=True)
    #cod_area = models.ForeignKey('Cod_Area', on_delete=models.SET_NULL, null=True)
    fono_c = models.CharField(max_length= 50, blank=True) 
    
    class Meta:
        ordering = ["apellido"]

    def __str__(self):
        return self.apellido+', '+self.user_gestor.first_name+'- '+ self.cargo
        #return self.apellido+self.cargo

#-----------------------------------
#--- ENTIDADES DEL FRAMEWORK -------
#-----------------------------------


class Framework(models.Model):
    """
    Entidad: Marco Metodologico 
    """
    numero = models.CharField(max_length=20, blank=True)                      #id. asignado por Sistema
    #codigo_frame= models.CharField(max_length=10, blank=True, unique=True)    #id. asignado por usuario
    fw_nombre = models.CharField(max_length=200, blank=True)
    fw_version= models.CharField(max_length=10, blank=True)
    fw_descrip= models.CharField(max_length=400, blank=True)
    fw_inst = models.CharField(max_length=150, blank=True)               #Institucion de origen del Framework

    fw_modulos =models.ForeignKey('Modulo_Mod', on_delete=models.SET_NULL,
                               related_name='auditor_sup',
                               null=True, blank=True)               #Auditor Supervisor
    
    #Correlativo de Modulos
    nro_modulos=models.IntegerField(default=0)

    def __str__(self):
        
        return self.fw_nombre+':'+self.fw_version


    
class Modulo_Mod(models.Model):
    """
    Entidad: Modulo del Framework
    """

    pk_frw   = models.IntegerField(default=0)                           #pk del framework asignado en su creacion
    pk_padre = models.IntegerField(default=0)
    numero = models.CharField(max_length=20, blank=True)                 #id. asignado por Sistema
    item = models.CharField(max_length=20,blank=True)
    nombre = models.CharField(max_length=100,blank=True)
    framework = models.ForeignKey(Framework, on_delete=models.SET_NULL,
                               related_name='framework',
                               null=True, blank=True)
    nro_submodulos = models.IntegerField(default=0)
    nro_objetivos  = models.IntegerField(default=0)
    abierto=models.BooleanField(default=False)

    class Meta:
        ordering = ["item"]

    def __str__(self):
        
        return self.item+' / '+self.nombre


class Obj_Ries_Mod(models.Model):
    """
    Entidad: Objetivo de Control/Riesgo del Framework
    """
    pk_padre = models.IntegerField(default=0)
    numero = models.CharField(max_length=20, blank=True)                 #id. asignado por Sistema
    obj_item = models.CharField(max_length=20,blank=True)
    obj_nombre = models.CharField(max_length=100,blank=True)
    obj_descripcion = models.CharField(max_length=600,blank=True)
    modulo = models.ForeignKey(Modulo_Mod, on_delete=models.SET_NULL,
                               related_name='modulo',
                               null=True, blank=True)
    
    class Meta:
        ordering = ["obj_item"]

    def __str__(self):
        
        return self.obj_item +' / '+self.obj_nombre

   

#---------------------------------
#--- ENTIDADES DE LA AUDITORIA ---
#---------------------------------


class Auditorias(models.Model):
    """
    Entidad: Auditoria
             Registra los atributos de un Proyecto de Auditoria
    """

    #Identificacion de la Auditoria
    numero = models.CharField(max_length=20, blank=True)           #id. asignado por Sistema
    cod_aud = models.CharField(max_length=20, blank=True, unique=True)          #identificacion asignado por Usuario
    nombre = models.CharField(max_length=100, blank=True)
    objetivo = models.CharField(max_length=600, blank=True)


    #Fechas de inicio y termino de la Auditoria
    fec_ini = models.DateField(null=True, blank=True)                
    fec_ter = models.DateField(null=True, blank=True)

    #Equipo Auditor
    auditor_sup = models.ForeignKey('Gestor', on_delete=models.SET_NULL,
                                related_name='auditor_sup',
                                null=True, blank=True)               #Auditor Supervisor
    auditor_ejec = models.ForeignKey('Gestor', on_delete=models.SET_NULL,
                                    related_name='auditor_ejec',
                                    null=True, blank=True)           #Auditor Ejecutor

    #Estado de la Auditoria
    PROC_STATUS = (
            ('S', 'Suspendida'),
            ('C', 'Cerrada'),
            ('E', 'Ejecucion'),
            ('P', 'Planificacion'),)

    status= models.CharField(max_length=1, choices=PROC_STATUS, blank=True, default='P', help_text='Estado de la definicion del Proceso')

    framework = models.ForeignKey(Framework, on_delete=models.SET_NULL, related_name='Frame_Work', null=True, blank=True)  

    #Correlativo de Modulos
    nro_modulos=models.IntegerField(default=0)


class Modulo(models.Model):
    """
    Entidad: Modulo del Framework
    """

    pk_aud  = models.IntegerField(default=0)                           #pk de la Auditoria asignado en su creacion
    pk_padre = models.IntegerField(default=0)
    numero = models.CharField(max_length=20, blank=True)               #id. asignado por Sistema
    item = models.CharField(max_length=20,blank=True)
    nombre = models.CharField(max_length=100,blank=True)
    auditoria = models.ForeignKey(Auditorias, on_delete=models.SET_NULL,
                               related_name='auditoria',
                               null=True, blank=True)
    nro_submodulos = models.IntegerField(default=0)
    nro_objetivos  = models.IntegerField(default=0)
    abierto=models.BooleanField(default=False)

    class Meta:
        ordering = ["item"]

    def __str__(self):
        
        return self.item+' / '+self.nombre

class Obj_Ries(models.Model):
    """
    Entidad: Objetivo de Control/Riesgo de la Auditoria
    """
    pk_padre = models.IntegerField(default=0)                            #pk del modulo padre
    numero = models.CharField(max_length=20, blank=True)                 #id. asignado por Sistema
    obj_item = models.CharField(max_length=20,blank=True)
    obj_nombre = models.CharField(max_length=100,blank=True)
    obj_descripcion = models.CharField(max_length=600,blank=True)
    modulo = models.ForeignKey(Modulo, on_delete=models.SET_NULL,
                               related_name='modulo_a',
                               null=True, blank=True)
    
    class Meta:
        ordering = ["obj_item"]

    def __str__(self):
        
        return self.obj_item +' / '+self.obj_nombre



#---------------------------------
#--- ENTIDADES MAESTRAS        ---
#---------------------------------


class Parametros_G(models.Model):
    """
    Parametros Generales del Sistema
    """
    nombre = models.CharField(max_length= 25, blank=True)
    valor_1 = models.CharField(max_length= 15, blank=True)
    valor_2 = models.IntegerField(null=True)
    #valor_3 = models.DecimalField(max_digits=7, decimal_places=4, default=000.00)


class Tipo_OC(models.Model):
    """
    Entidad: Tipo de Objetivo de Control/Riesgo
    """

    tipo_oc_nombre = models.CharField(max_length=20, blank=True)
    tipo_oc_descripcion = models.CharField(max_length=300, blank=True)
