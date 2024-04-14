#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual: salários até R 280,00(incluindo):aumentode20saláriosentreR  280,00 e R 700,00:aumentode15saláriosentreR  700,00 e R 1500,00:aumentode10saláriosdeR  1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela: o salário antes do reajuste; o percentual de aumento aplicado; o valor do aumento; o novo salário, após o aumento.
salario = float(input("Digite o salário do colaborador: "))

if salario <= 280.00:
    percentual_aumento = 20
elif salario <= 700.00:
    percentual_aumento = 15
elif salario <= 1500.00:
    percentual_aumento = 10
else:
    percentual_aumento = 5

aumento = salario * (percentual_aumento / 100)
novo_salario = salario + aumento

print(f"Salário antes do reajuste: R${salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento:.0f}%")
print(f"Valor do aumento: R${aumento:.2f}")
print(f"Novo salário, após o aumento: R${novo_salario:.2f}")
