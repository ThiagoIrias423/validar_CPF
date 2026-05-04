# 🛡️ CPF Validator: Lógica e Implementação em Python

Este projeto implementa um validador de **Cadastro de Pessoas Físicas (CPF)** eficiente e didático. O foco não é apenas verificar o formato, mas garantir a integridade matemática do documento através do algoritmo oficial da Receita Federal.

## 📖 Guia de Estudo: Como funciona a validação?

O algoritmo presente neste código segue três etapas cruciais para garantir que um CPF seja genuíno:

1.  **Saneamento e Pré-Verificação**: O código limpa a entrada, removendo pontos e traços com `filter(str.isdigit)`, restando apenas números. Ele também invalida CPFs com 11 dígitos idênticos (ex: `111.111.111-11`), pois, embora matematicamente "corretos" em certas fórmulas, são considerados inválidos.
2.  **Cálculo do 1º Dígito Verificador**: Multiplicamos os primeiros 9 dígitos por pesos decrescentes de 10 a 2. A soma desses produtos é multiplicada por 10 e o resto da divisão por 11 nos dá o primeiro dígito (se for maior que 9, vira 0).
3.  **Cálculo do 2º Dígito Verificador**: O processo é repetido incluindo o primeiro dígito recém-calculado, desta vez com pesos de 11 a 2.

## 💻 Detalhes Técnicos

A função principal `validar_cpf(cpf: str) -> bool` foi otimizada para ser concisa e rápida:

-   **Eficiência**: Utiliza *List Comprehension* e a função `sum()` para realizar as somas ponderadas de forma dinâmica.
-   **Flexibilidade**: Aceita strings com ou sem formatação (pontos e hífens).
-   **Segurança**: Retorna um valor booleano puro (`True` ou `False`), facilitando a integração em sistemas maiores.

## 🧪 Casos de Teste e Exemplos

| Entrada (Input) | Comportamento Interno | Resultado |
| :--- | :--- | :--- |
| `123.456.789-00` | Limpeza -> Cálculo de Dígitos | Válido/Inválido conforme cálculo |
| `11111111111` | Detectado como sequência repetida | **Inválido** |
| `12345` | Detectado comprimento incorreto | **Inválido** |

## 🚀 Como executar

Basta rodar o arquivo e inserir o CPF quando solicitado pelo `input()`:
```bash
