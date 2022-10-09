# Urna

Você foi convocado para escrever o novo algoritmo da urna para as próximas eleições!

## Requisitos

- A urna deve ser capaz de cadastrar candidatos
  - Cada candidato deve ter um nome e um número
  - O número do candidato deve ser único
- A urna deve ser capaz de receber votos
  - Permita o voto em branco
  - Permita o voto nulo
  - Caso o número do candidato não exista, o voto deve ser computado como nulo
  - Confirme o voto antes de computá-lo
- A urna deve ser capaz de contar os votos e dar o resultado da votação
  - O resultado deve ser exibido em ordem decrescente de votos
  - Considere que os votos em branco irão para o candidato com o maior número de votos
  - Em caso de empate, o candidato com o menor número deve aparecer primeiro
  - O resultado deve ser exibido no seguinte formato: `NOME (NÚMERO) - VOTOS`

## Dicas

- Use um dicionário para armazenar os candidatos
- Use um dicionário para armazenar os votos
- Use funções para cada etapa do algoritmo

## Exemplo

```
        1 - Cadastrar candidato
        2 - Votar
        3 - Resultado
        4 - Sair
        
Digite a opção desejada: 1
Digite o nome do candidato: Gabriel
Digite o número do candidato: 99

        1 - Cadastrar candidato
        2 - Votar
        3 - Resultado
        4 - Sair
        
Digite a opção desejada: 2
Digite o número do candidato: 99
Confirme o voto em Gabriel (s/n)? s

        1 - Cadastrar candidato
        2 - Votar
        3 - Resultado
        4 - Sair
        
Digite a opção desejada: 2
Digite o número do candidato: 7
Confirme o voto em nulo (s/n)? s

        1 - Cadastrar candidato
        2 - Votar
        3 - Resultado
        4 - Sair
        
Digite a opção desejada: 3
Resultado:
Nulo - 1
Gabriel (99): 1

        1 - Cadastrar candidato
        2 - Votar
        3 - Resultado
        4 - Sair
        
Digite a opção desejada: 4
Sair
```

## Desafio

Permita a votação para todos os possíveis cargos. Sendo eles:

- Presidente
- Governador
- Senador
- Deputado Federal
- Deputado Estadual

Para que isso seja possível, você deve:

1. Modificar o cadastro para que seja possível cadastrar candidatos para cada um dos cargos.
2. Modificar o voto para que seja possível votar em todos os cargos.
3. Modificar o resultado para que seja possível ver o resultado de cada um dos cargos.
