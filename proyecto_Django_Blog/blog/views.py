from django.shortcuts import render

from .models import Post


def blog_home(request):
    """
    Vista principal del blog.
    Recupera todas las publicaciones y las ordena de la más reciente a la más antigua.
    Conecta los datos con la plantilla HTML (patrón MVT de Django).
    """
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/home.html', {'posts': posts})

