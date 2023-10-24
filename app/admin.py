from django.contrib import admin
from .models import Comunicado, Entidad
from django.http import HttpResponseForbidden

class datos_comunicado(admin.ModelAdmin):
    list_display=("titulo","tipo","entidad","fecha_publicacion","fecha_ultima_modificacion", "publicado_por", "modificado_por")
    list_filter=("fecha_publicacion",)

    def save_model(self, request, obj, form, change):

        if not request.user.is_superuser:

            if change and (str(obj.entidad) != str(request.user.groups.get())): 
                return HttpResponseForbidden("No tienes permiso para editar este comunicado.")

            elif not change:  #Para crear un comunicado
                obj.publicado_por = request.user

            else: #Para modificar un comunicado
                obj.modificado_por = request.user

        else:

            if not change:  #Para crear un comunicado
                obj.publicado_por = request.user

            else: #Para modificar un comunicado
                obj.modificado_por = request.user
                
        super().save_model(request, obj, form, change)


admin.site.register(Entidad)
admin.site.register(Comunicado, datos_comunicado)


