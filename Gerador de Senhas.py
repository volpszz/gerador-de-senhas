import random
import string

def gerar_senha(tamanho):

    # Define os caracteres permitidos

    caracteres = string.ascii_letters + string.digits + string.punctuation 
    senha = ''.join(random.choices(caracteres, k=tamanho))

    return senha

while True:
    try:

# Solicita o tamanho da senha ao usuário

        tamanho = int(input("Digite o tamanho da senha: "))

# Gera e exibe a senha

        print("Sua senha gerada é:", gerar_senha(tamanho))  
    
        break
    
    except ValueError:
        print("Erro, por favor digite um número valido!")



