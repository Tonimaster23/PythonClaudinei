# test_funcoes.py

import pytest
from funcoes import (email_valido, eh_par, fatorial, quadrado, eh_positivo,
                     verificar_maioridade, classificar_temperatura,
                     avaliar_nota, pode_votar, avaliar_produto)

def test_email_valido():
    assert email_valido("teste@exemplo.com") == True
    assert email_valido("invalido@com") == False

def test_eh_par():
    assert eh_par(4) == True
    assert eh_par(5) == False

def test_fatorial():
    assert fatorial(0) == 1
    assert fatorial(5) == 120

def test_quadrado():
    assert quadrado(3) == 9
    assert quadrado(-3) == 9

def test_eh_positivo():
    assert eh_positivo(5) == True
    assert eh_positivo(-5) == False

def test_verificar_maioridade():
    assert verificar_maioridade(20) == 'maior de idade'
    assert verificar_maioridade(16) == 'menor de idade'

def test_classificar_temperatura():
    assert classificar_temperatura(-5) == 'frio'
    assert classificar_temperatura(20) == 'moderado'
    assert classificar_temperatura(30) == 'quente'

def test_avaliar_nota():
    assert avaliar_nota(8) == 'aprovado'
    assert avaliar_nota(6) == 'recuperacao'
    assert avaliar_nota(4) == 'reprovado'

def test_pode_votar():
    assert pode_votar(20) == 'voto obrigatório'
    assert pode_votar(17) == 'voto facultativo'
    assert pode_votar(15) == 'não pode votar'

def test_avaliar_produto():
    assert avaliar_produto(5) == 'excelente'
    assert avaliar_produto(3) == 'regular'
    assert avaliar_produto(0) == 'valor inválido'
