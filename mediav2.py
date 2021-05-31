# Font color
reset_color = "\033[0m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
cyan = "\033[1;36;40m"
magenta = "\033[1;35;40m"
# ===================================
import os
os.system('cls' if os.name == 'nt' else 'clear')

print(yellow+ "="*50)
print("=            Boas Vindas ao Média 2.0            =")
print("="*50 +reset_color)
print("")

input(green+ "Prescione (ENTER) pra continuar ou (Ctl+C) para sair: " +reset_color)

import os
os.system('cls' if os.name == 'nt' else 'clear')

print(green+ "V2.0")
print("-----" +reset_color)
print(yellow+ "")

nome = str(input("Nome do aluno: "))

import os
os.system('cls' if os.name == 'nt' else 'clear')

print(green+"V2.0")
print("-----" +reset_color)
print(yellow+ "")

minima = float(input("Informe a nota mínima: "))

os.system('cls' if os.name == 'nt' else 'clear')

print(green+"V2.0")
print("-----" +reset_color)
print("")

n1 = float(input("Informe a nota do primeiro bimestre: "))
print("")
n2 = float(input("Informe a nota do segundo bimestre: "))
print("")
n3 = float(input("Informe a nota do terceiro bimestre: "))
print("")
n4 = float(input("Informe a nota do quarto bimestre: "))
print("")


soma = n1 + n2 + n3 + n4
media = soma/4 

import os
os.system('cls'if os.name =='nt' else 'clear')

print(green+"V2.0")
print("-----" +reset_color)

if media<minima:
    print("="*35)
    print("Aluno(a), {}:".format(nome))
    print("")
    print(red+ "Reprovado(a)!" +reset_color)
    print("Nota: {}".format(media))
    print("Mínima: {}".format(minima))
    print("="*35)
else:
    print("="*35)
    print("Aluno(a), {}:".format(nome))
    print("")
    print(green+ "Aprovado(a)!" +reset_color)
    print("Nota: {}".format(media))
    print("Mínima: {}".format(minima))
    print("="*35)

print("")

input(green+ "Prescione <ENTER> para sair: " +reset_color)