import random

print('Olá, vou criar sua senha! :)')

caracters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*?0123456789'
numero = input('Quantas senhas precisa?: ')
numero = int(numero)

tamanho = input('Qual tamanho dessa senha?: ')
tamanho = int(tamanho)

print('\n Aqui estão suas senhas!: ')

for senha in range(numero):
    senha = ''
    for c in range(tamanho):
        senha += random.choice(caracters)
    print(senha)
