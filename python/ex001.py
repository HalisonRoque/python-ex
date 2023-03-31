nome = 'HALISON'
numero = '111111111e'
print(nome)

print(type(nome)) # mostra o tipo de classe é essa variavel

print(nome.capitalize())  # transforma em letra maiuscula a primeira letra do nome  

print(nome.upper()) #transforma todas as letras em maiusculas

print(nome.casefold()) # transforma todas as letras em letras minisculas

print(nome.replace('o', 'a', 1)) # troca determminada letra por outra letra, indica tbm quantas letras devem ser trocadas

print(numero.isnumeric()) #verifica se a string é toda numerica = retorno bool
print(nome.isalpha()) # verifica se a string so contem letras = retorno bool
print(numero.isalnum()) # verifica se a string contem letras e numeros = retorno bool
print(nome.isupper()) # verifica se a string esta toda em letras maiusculas = retorno bool
print(nome.islower()) # verifica se a string esta toda em letras minisculas = retorno bool
nome1 = 'halison, roque'
numero1 = '1111111er'
print(nome1.find('r')) #retorna a posição da letra indicada na string

print(nome1.split(',')) #esse metodo separa as string, por padrao separa onde contem espaços, mas pode dar o parametro.
















