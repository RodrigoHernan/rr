from django.contrib import admin
from .models import Grupo  , Tarea
# Register your models here.

class GrupoAdminInline(admin.TabularInline):
    model = Tarea
class GrupoAdmin(admin.ModelAdmin):
    inlines = (GrupoAdminInline, )

class AdminTarea(admin.ModelAdmin):
    list_display = ['nombre' , 'time', 'hecho' ,'grupo' ]
    ordering = ['time']
    list_filter = ['hecho']


admin.site.register(Tarea , AdminTarea)
admin.site.register(Grupo, GrupoAdmin)