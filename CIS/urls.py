#Programa PYTHON
#Definicion de Links urls
#Programado por Marco A. Villalobos Michelson
#=============================================

from django.urls import re_path as url
from django.urls import path 

from . import views

#Pagina Principal
urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    ]

#Frameworks
urlpatterns += [
    path(r'^Frameworks/$', views.Lista_Framew, name='Lista-Framework'),
    path(r'^Frameworks/crea_frame/$', views.Crea_Frame, name='Crea-Framework'),
    path(r'^Frameworks/(?P<pk>\d+)/borra_frame/$', views.Borra_Framework, name='Borra-Framework'),
    path(r'^Frameworks/(?P<pk>\d+)/lista_mod_mod/$', views.Lista_Mod_M, name='Lista-Mod-M'),
    path(r'^Frameworks/(?P<pk>\d+)/crea_mod_mod/$', views.Crea_Mod_Mod, name='Crea-Mod-M'),
    path(r'^Frameworks/(?P<pk>\d+)/borra_mod_mod/$', views.Borra_Mod_Mod, name='Borra-Mod-M'),
    path(r'^Frameworks/(?P<pk>\d+)/crea_oc/$', views.Crea_OC_Mod, name='Crea-OC-M'),
    path(r'^Frameworks/(?P<pk>\d+)/borra_oc/$', views.Borra_OC_Mod, name='Borra-OC-M'),
    path(r'^Frameworks/(?P<pk>\d+)/modifica_oc/$', views.Mod_OC_Mod, name='Mod-OC-M'),
    path(r'^Frameworks/(?P<pk>\d+)/abre_cierra/$', views.Abre_Cierra, name='Abre-Cierra'),

    #Exportar a Excel
    path(r'^Frameworks/(?P<pk>\d+)/exp_frame_to_exel/$', views.Export_Frame_to_Exel, name='Exp-FrametoExcel'),

    ]

#Auditorias
urlpatterns += [
    path(r'^Auditorias/$', views.Lista_Auditorias, name='Lista-Auditorias'),
    path(r'^Auditorias/crea_audit/$', views.Crea_Auditoria, name='Crea-Auditoria'),
    path(r'^Auditorias/(?P<pk>\d+)/lista_mod/$', views.Lista_Mod, name='Lista-Mod'),
    path(r'^Auditorias/(?P<pk>\d+)/crea_mod/$', views.Crea_Mod, name='Crea-Mod'),
    path(r'^Auditorias/(?P<pk>\d+)/borra_mod/$', views.Borra_Mod, name='Borra-Mod'),
    path(r'^Auditorias/(?P<pk>\d+)/crea_oc_a/$', views.Crea_OC, name='Crea-OC'),
    path(r'^Auditorias/(?P<pk>\d+)/borra_oc_a/$', views.Borra_OC, name='Borra-OC'),
    path(r'^Auditorias/(?P<pk>\d+)/abre_cierra_a/$', views.Abre_Cierra_A, name='Abre-Cierra-A'),

    #Exportar a Excel
    path(r'^Auditorias/(?P<pk>\d+)/exp_audit_to_exel/$', views.Export_audit_to_Exel, name='Exp-AudittoExcel'),

    #Importar desde Excel
    path(r'^Auditorias/imp_audit_from_exel/$', views.seleccionar_archivo, name='Imp-AuditfromExcel'),

]
