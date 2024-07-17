from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.


#*** FrameWork ***
from .models import  Obj_Ries_Mod, Modulo_Mod, Modulo, Framework, Parametros_G, Obj_Ries

@admin.register(Framework)
class AdminFramework(admin.ModelAdmin):
    list_display = ('numero', 'fw_nombre', 'fw_descrip', 'fw_inst','fw_version','nro_modulos')

@admin.register(Modulo_Mod)
class AdminModulo_Mod(admin.ModelAdmin):
    list_display = ('pk_padre', 'pk_frw', 'numero','nombre', 'item')


@admin.register(Obj_Ries_Mod)
class AdminObj_Ries_Mod(admin.ModelAdmin):
    list_display = ('numero', 'pk_padre', 'obj_nombre', 'obj_item')


#*** Auditoria ***
from .models import  Auditorias

@admin.register(Auditorias)
class AdminAudit(admin.ModelAdmin):
    list_display = ('numero', 'cod_aud', 'nombre','objetivo','fec_ini','fec_ter', 'status')

@admin.register(Modulo)
class AdminModulo(admin.ModelAdmin):
    list_display = ('pk_padre', 'pk_aud', 'numero','nombre', 'item', 'nro_submodulos')

@admin.register(Obj_Ries)
class AdminObj_Ries(admin.ModelAdmin):
    list_display = ('numero','obj_nombre', 'obj_item')
    

#*** Datos Fijos ***
from .models import  Gestor, Tipo_OC

@admin.register(Gestor)
class AdminGestor(admin.ModelAdmin):
    list_display = ('apellido','user_pk','user_gestor', 'cargo', 'fono_t', 'fono_c')

@admin.register(Tipo_OC)
class AdminTipo_OC(admin.ModelAdmin):
    list_display = ('tipo_oc_nombre', 'tipo_oc_descripcion')


@admin.register(Parametros_G)
class AdminParametros_G(admin.ModelAdmin):

    list_display = ('nombre', 'valor_1', 'valor_2')


