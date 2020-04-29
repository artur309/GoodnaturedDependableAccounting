#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os import *

def nome_turma_aluno(lista_turma):
    contador=1
    for i in range(len(lista_turma)):
            print("ALUNO Nº", contador)
            lista_turma[i]=input("NOME: ")
            contador+=1
            print("")
    return

def listar_turmas(lista_turma):
    contador=1
    for i in range(len(lista_turma)):
            print("ALUNO ", contador)
            print(lista_turma[i])
            contador+=1
            print("")
    return


turma1=int(input("Quantos alunos estao na turma 1: "))
turma2=int(input("Quantos alunos estao na turma 2: "))
turma3=int(input("Quantos alunos estao na turma 3: "))

lista_turma1=[0]*turma1
lista_turma2=[0]*turma2
lista_turma3=[0]*turma3

print("")

print("TURMA 1\n")
nome_turma_aluno(lista_turma1)

print("------------------------------------------------------------------------")

print("TURMA 2\n")
nome_turma_aluno(lista_turma2)

print("------------------------------------------------------------------------")

print("TURMA 3\n")
nome_turma_aluno(lista_turma3)

os.system("cls")

print("APRESENTAÇÂO DAS TURMAS")

print("TURMA 1\n")
listar_turmas(lista_turma1)

print("------------------------------------------------------------------------")

print("TURMA 2\n")
listar_turmas(lista_turma2)

print("------------------------------------------------------------------------")

print("TURMA 3\n")
listar_turmas(lista_turma3)

input("\nenter")