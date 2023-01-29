import random

# Tipos de caracteres possíveis de uso
characters_lower = "abcdefghijklmnopqrstuvwxyz"
characters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "*._-@!#&$"

# Juntando todos os tipos de caracteres em uma variavel
all = characters_lower + characters_upper + numbers + symbols

# O usuario informa o numero de caracteres desejado
number_of_characters = int(input('Quantos caracteres a senha deve ter ?'))

# Misturando os caracteres e criando a senha
password = "".join(random.sample(all, number_of_characters))

# Mostrando a senha em tela
print(f'Sua senha é: ( \033[32m {password} \033[m )')
