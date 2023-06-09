from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.usuariolist, name="usuario_list")
]
