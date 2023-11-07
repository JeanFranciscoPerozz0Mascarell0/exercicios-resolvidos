#Uma imobiliária paga aos seus corretores um salário base de R$ 1.500,00. 
#Além disso, uma comissão de R$ 200,00 por cada imóvel vendido e 
#5% do valor de cada venda. Construa um programa que solicite o nome do corretor, 
#a quantidade de imóveis vendidos e o valor total de suas vendas. 
#Ao fim, o programa deve calcular e escrever o salário final do corretor de imóveis.

salario_fixo = 1500.00
comissao = 0

nome = input("Digite o nome do vendedor: ")
imoveis_vendidos = int(input("Digite a quantidade de imoveis que foi vendido: "))
empresa_saldo = 0

for vendas in range(0,imoveis_vendidos):
    valor_venda = float(input("Qual o valor da sua venda: R$ "))
    empresa_saldo += valor_venda
    comissao_porcentagem_venda = valor_venda * 0.05
    comissao += comissao_porcentagem_venda
    comissao_por_venda = 200 * (vendas + 1)


salario_total = comissao_por_venda + comissao + salario_fixo

print(f"\nVendeu: {imoveis_vendidos}.")
print(f"Salario mensal total de {nome}: R$ {salario_total:.2f}.")
print(f"Lucro da empresa este mes: {empresa_saldo}.\n")