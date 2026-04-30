#Criação da função onde inserir os parametros para validação do CPF
def validar_cpf(cpf: str) -> bool:

#Filtragem para quando o usuário digitar o cpf o código ler apenas os números, pois ocpf será lido como string
    cpf = '' .join(filter(str.isdigit,cpf))

#Definido quantos caracteres devem ter e impedindo um sequência de números iguais
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

#Conversão do CPF em números inteiros e calculo do primeiro digito validador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    digito1 = digito1 if digito1 < 10 else 0

#Calculo do segundo digito validador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    digito2 = digito2 if digito2 < 10 else 0

#Verifica se os digitos obtidos pelo calculo batem com os fornecidos pelo usuário
    return cpf[-2:] == f"{digito1}{digito2}"

#Entrada para usuário
cpf = input('Digite o seu CPF: ')

#Executa a função e responde para o usuário
if validar_cpf(cpf):
    print('CPF válido')
else:
    print('CPF inválido')
