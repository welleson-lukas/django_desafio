from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..services import service
from ..serializer import pessoas_serializer
from ..entidades import pessoas
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class PessoasList(APIView):
    def get(self, request, format=None):
        paginacao = PageNumberPagination() # A QUANTIDADE DE RESULTADOS NA PAGINAÇÃO ESTÃO DEFINIDOS NO settings.py
        pessoas = service.listar_pessoas()
        resultado = paginacao.paginate_queryset(pessoas, request)
        serializer = pessoas_serializer.PessoasSerializer(resultado, many=True)
        return paginacao.get_paginated_response(serializer.data)
        #return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = pessoas_serializer.PessoasSerializer(data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            cidade = serializer.validated_data["cidade"]
            data_nascimento = serializer.validated_data["data_nascimento"]
            pessoa_nova = service.Pessoas(nome=nome, cidade=cidade, data_nascimento=data_nascimento)
            service.cadastrar_pessoa(pessoa_nova)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


class PessoasDetalhes(APIView):

    def get(self, request, id, format=None):
        pessoas = service.listar_pessoa_id(id)
        serializer = pessoas_serializer.PessoasSerializer(pessoas)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        pessoa_antigo = service.listar_pessoa_id(id)
        serializer = pessoas_serializer.PessoasSerializer(pessoa_antigo, data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            cidade = serializer.validated_data["cidade"]
            data_nascimento = serializer.validated_data["data_nascimento"]

            pessoa_novo = pessoas.Pessoas(nome=nome, cidade=cidade, data_nascimento=data_nascimento)
            service.editar_pessoa(pessoa_antigo, pessoa_novo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        pessoa = service.listar_pessoa_id(id)
        service.remover_pessoa(pessoa)
        return Response(status=status.HTTP_204_NO_CONTENT)