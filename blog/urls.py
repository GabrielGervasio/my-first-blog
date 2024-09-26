from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.post_list, name='post_list'),
    path('cadastro', views.cadastrar_usuario, name='cadastro'),
    path('login', views.entrar, name='login'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('equipes', views.equipes, name='equipes'),
    path('equipe/<int:pk>/', views.equipe_detail, name='equipe_detail'),
    path('palestra', views.palestra, name='palestra'),
    path('atletica', views.atletica, name='atletica'),
    path('atletica/<int:atletica_id>/', views.detalhes_atletica, name='detalhes_atletica'),
    path('projeto', views.projeto, name='projeto'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


