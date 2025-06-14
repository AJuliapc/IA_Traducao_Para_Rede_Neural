import csv
import itertools

# Nome das variáveis
variaveis = ['A', 'B', 'C', 'D']

# Gera todas as combinações possíveis de 1 e -1
combinacoes = list(itertools.product([1, -1], repeat=len(variaveis)))

# Salva em um CSV
with open("entradas_logicas.csv", mode="w", newline="") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(variaveis)  # Cabeçalho
    writer.writerows(combinacoes)

print("Arquivo 'entradas_logicas.csv' gerado com sucesso!")
