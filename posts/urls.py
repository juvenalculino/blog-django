from django.urls import path
from . import views
from . import settings
from . import static

urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('categoria/<str:categoria>', views.PostCategoria.as_view(), name='post_categoria'),
    path('busca/', views.PostBusca.as_view(), name='post_busca'),
    path('post/<int:pk>', views.PostDetalhes.as_view(), name='post_detalhes'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)