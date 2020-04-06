from django.urls import path
from .views import view

urlpatterns = [
    path('pessoas/', view.PessoasList.as_view(), name='pessoas-list'),
    path('pessoas/<int:id>', view.PessoasDetalhes.as_view(), name='pessoas-detalhes'),

]
