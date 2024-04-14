#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R 80,00ouemgalõesde3,6litros,quecustamR  25,00.Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
• comprar apenas latas de 18 litros; • comprar apenas galões de 3,6 litros; • misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

tamanho_area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
cobertura_por_litro = 6

litros_necessarios = tamanho_area / cobertura_por_litro

latas_necessarias = math.ceil(litros_necessarios / 18)
preco_latas = latas_necessarias * 80

galoes_necessarios = math.ceil(litros_necessarios / 3.6)
preco_galoes = galoes_necessarios * 25

mix_latas = math.ceil(litros_necessarios / 18)
mix_galoes = math.ceil((litros_necessarios % 18) / 3.6)
preco_mix = (mix_latas * 80) + (mix_galoes * 25)

print(f"Comprar apenas latas de 18 litros: {latas_necessarias} latas, Preço: R${preco_latas:.2f}")
print(f"Comprar apenas galões de 3,6 litros: {galoes_necessarios} galões, Preço: R${preco_galoes:.2f}")
print(f"Misturar latas e galões: {mix_latas} latas e {mix_galoes} galões, Preço: R${preco_mix:.2f}")
