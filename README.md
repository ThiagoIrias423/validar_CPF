# validar_CPF
Criação de um código que identifique um CPF e defina ele como válido ou inválido

Validação de CPF em Python 🐍
Este projeto implementa uma função robusta para validar CPFs brasileiros, garantindo que o número siga as regras matemáticas oficiais.
🎯 Objetivo
-Limpar formatações (pontos e traços).
-Verificar dígitos verificadores usando pesos matemáticos.
-Identificar sequências inválidas (ex: 111.111.111-11).
🛠️ Como Funciona
-Limpeza: Filtra apenas números usando filter(str.isdigit, cpf).
-Validação Inicial: Checa se possui 11 dígitos e se não são todos iguais.
-Cálculo de Dígitos: Aplica a lógica de pesos (10 a 2 e 11 a 2) para validar os dois últimos números.
🚀 Exemplo de Uso
if validar_cpf('123.456.789-00'):
    print('Válido'
