# leitura dos dados 
nome = input('digite o nome do vendedor')
salario_fixo = float(input("digite o salario fixo:"))
total_vendas = float(input("digite o total de vendadas do més:"))

# cálculo da comissão (15% sobre as vendas) 
comissao = total_vendas * 0.15 

# calculo do total a receber 
total_receber = salario_fixo + comissao

# saida formata 
print(f"TOTAL = R${total_receber:.2f}")
print(nome)