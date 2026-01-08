import csv

# Caminho do CSV
caminho_csv = "Dados/vendas.csv"  

# Listas para armazenar dados
produtos = []
quantidades = []
precos = []

# Lendo o CSV
with open(caminho_csv, newline='', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=';')  # ponto e vírgula
    for linha in leitor:
        produtos.append(linha['produto'])
        quantidades.append(int(linha['quantidade']))
        precos.append(float(linha['preco']))

# Calculando faturamento total
faturamento_total = sum(q * p for q, p in zip(quantidades, precos))

# Produto mais vendido
mais_vendido = produtos[quantidades.index(max(quantidades))]

# Valor médio por item
valor_medio = faturamento_total / sum(quantidades)

# Relatório
print("Relatório de Vendas\n")
print(f"Faturamento total: R$ {faturamento_total:,.2f}")
print(f"Produto mais vendido: {mais_vendido}")
print(f"Valor médio por item vendido: R$ {valor_medio:,.2f}")
