def validar_cpf(cpf: str) -> bool:

    cpf = '' .join(filter(str.isdigit,cpf))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    digito1 = digito1 if digito1 < 10 else 0

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    digito2 = digito2 if digito2 < 10 else 0

    return cpf[-2:] == f"{digito1}{digito2}"


cpf = input('Digite o seu CPF: ')

if validar_cpf(cpf):
    print('CPF válido')
else:
    print('CPF inválido')