import random
import os

os.system('cls')

print('***************************************************')
print('********* BEM-VINDO AO SIMULADOR DE DADOS *********')
print('***************************************************\n')

quantidade_dados = int(input('Quantos dados você deseja rolar? '))

os.system('cls')

print('Resultado da rolagem: \n')

for dado in range(quantidade_dados):
    dado += 1
    print(dado,'° dado: ', random.randint(1,6))

print('\n')





    



















