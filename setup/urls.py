
from django.urls import path
from django.conf.urls.static import static
from setup import settings

from catalogo.views import FilmeCreateView, FilmeDeleteView, FilmeDetailView, FilmeListView, FilmeUpdateView, CatalogoCreateView, CatalogoDeleteView, CatalogoDetailView, CatalogoListView, CatalogoUpdateView

urlpatterns = [
    path('', CatalogoListView.as_view(), name='catalogo_list'),
    path('create/', CatalogoCreateView.as_view(), name='catalogo_create'),
    path('<int:pk>/', CatalogoDetailView.as_view(), name='catalogo_detail'),
    path('<int:pk>/edit/', CatalogoUpdateView.as_view(), name='catalogo_update'),
    path('<int:pk>/delete/', CatalogoDeleteView.as_view(), name='catalogo_delete'),

    path('filme/', FilmeListView.as_view(), name='filme_list'),
    path('filme/<int:pk>/', FilmeDetailView.as_view(), name='filme_detail'),
    path('filme/create/', FilmeCreateView.as_view(), name='filme_create'),
    path('filme/<int:pk>/edit/', FilmeUpdateView.as_view(), name='filme_update'),
    path('filme/<int:pk>/delete/', FilmeDeleteView.as_view(), name='filme_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),