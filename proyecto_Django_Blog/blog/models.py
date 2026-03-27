from django.db import models


class Post(models.Model):
    """
    Modelo que representa una publicación del blog.
    Cada atributo corresponde a una columna en la base de datos (ORM de Django).
    """
    title = models.CharField(max_length=200)                    # Texto corto para el título.
    content = models.TextField()                                # Texto largo para el contenido.
    published_date = models.DateTimeField(auto_now_add=True)    # Fecha que se guarda automáticamente al crear.

    def __str__(self):
        """Representación legible del objeto en el panel de administración."""
        return self.title
