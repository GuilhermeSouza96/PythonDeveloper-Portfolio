import re
from validate_docbr import CPF

def invalid_cpf(number_cpf):
    cpf = CPF()
    valid_cpf = cpf.validate(number_cpf)
    return not valid_cpf


def invalid_name(name):
    return not name.isalpha()

def invalid_phone(phone):
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(model, phone)
    return not response
