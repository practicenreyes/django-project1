from django.contrib import admin
from app.models import Enlace, Categoria, Agregador

from app.actions import export_as_csv
# Register your models here.

class EnlaceAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'enlace', 'categoria', 'imagen_voto', 'es_popular')
	list_filter = ('categoria', 'usuario')
	search_fields = ('categoria__titulo', 'usuario__email')
	list_editable = ('titulo', 'enlace', 'categoria')
	actions = [export_as_csv]
	raw_id_fields = ('categoria', 'usuario')

	def imagen_voto(self, obj):
		u = obj.mis_votos_en_imagen_rosada()
		tag = '<img src="%s" />' %(u)
		return tag
	imagen_voto.allow_tags = True
	imagen_voto.admin_order_field = "votos"

class EnlaceInline(admin.StackedInline):
	model = Enlace
	extra = 3
	raw_id_fields = ('usuario',)

class CategoriaAdmin(admin.ModelAdmin):
	actions = [export_as_csv]
	inlines = [EnlaceInline]

class AgregadorAdmin(admin.ModelAdmin):
	filter_horizontal = ('enlaces',)

admin.site.register(Agregador, AgregadorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Enlace, EnlaceAdmin)