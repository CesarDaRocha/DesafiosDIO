import re

def validate_numero_telefone(phone_number):
    pattern = r'\(\d{2}\)\s9\d{4}-\d{4}'
    if re.match(pattern, phone_number):
        return 'O número de telefone é válido.'
    else:
        return 'O número de telefone é inválido.'

phone_number = input('Digite um número de telefone no formato (XX) 9XXXX-XXXX: ')
result = validate_numero_telefone(phone_number)
print(result)
