from django.http import Http404
from ..models import Pessoas

def listar_pessoas():
    pessoas = Pessoas.objects.all()
    return pessoas

def cadastrar_pessoa(pessoa):
    return Pessoas.objects.create(nome=pessoa.nome, cidade=pessoa.cidade, data_nascimento=pessoa.data_nascimento)

def listar_pessoa_id(id):
    try:
        return Pessoas.objects.get(id=id)
    except Pessoas.DoesNotExist:
        raise Http404

def editar_pessoa(pessoa_antigo, pessoa_novo):
    pessoa_antigo.nome = pessoa_novo.nome
    pessoa_antigo.cidade = pessoa_novo.cidade
    pessoa_antigo.data_nascimento = pessoa_novo.data_nascimento
    pessoa_antigo.save(force_update=True)

def remover_pessoa(pessoa):
    pessoa.delete()



