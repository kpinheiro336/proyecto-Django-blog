from django.contrib import admin

from .models import Post

# Personalización del encabezado y título del panel de administración
admin.site.site_header = '📚 Librería Folium'
admin.site.site_title = 'Admin Librería Folium'
admin.site.index_title = 'Panel de administración'

# Registro del modelo Post para que sea gestionable desde el admin.
admin.site.register(Post)

