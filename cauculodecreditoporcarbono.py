import datetime
import math

empresa = str(input('Digite o nome da sua empresa: '))

hora_atual = datetime.datetime.now().hour
bomdia = ""
if hora_atual < 12:
    bomdia += 'Bom dia!'
elif 12 <= hora_atual < 18:
    bomdia += 'Boa tarde!'
else:
    bomdia += 'Boa noite!'
print(bomdia)
print(f"Estamos felizes em saber que o(a),\033[1;32m {empresa}\033[m, tem se preocupado com a emissão "
      f"de gases de seus maquinários e segue a linha do desinvolvimento sustentável!")
print()
print("Primeiro, vamos precisar de alguns dados da sua empresa!")
print()
carbonoTotal = 0

dinheiroCombustivel = float(input('Qual a média mensal de gasto da sua empresa com combustível?: R$'))

tipoCombustivel = int(input('Qual o tipo de combustível majoritário da sua empresa?\nUse \033[1;31m1 = Disel, '
                            '\033[1;32m2 = Gasolina, \033[1;33m3 = Etanol, \033[1;34m4 = Gás Natural\033[m : '))
while (tipoCombustivel > 4) or (tipoCombustivel < 1):
    print()
    print("Código de combustível inválido!\n \033[1;31mTENTE NOVAMENTE!\033[m")
    print()
    tipoCombustivel = int(input('Qual o tipo de combustível majoritário da sua empresa?\nUse \033[1;31m1 = Disel, '
                                '\033[1;32m2 = Gasolina, \033[1;33m3 = Etanol, \033[1;34m4 = Gás Natural\033[m : '))

if tipoCombustivel == 1:
    combustivel = dinheiroCombustivel * 0.0042
    carbonoTotal += combustivel
elif tipoCombustivel == 2:
    combustivel = dinheiroCombustivel * 0.003504
    carbonoTotal += combustivel
elif tipoCombustivel == 3:
    combustivel = dinheiroCombustivel * 0.000024
    carbonoTotal += combustivel
elif tipoCombustivel == 4:
    combustivel = dinheiroCombustivel * 0.006708
    carbonoTotal += combustivel
print()
print(f"Você emite por meio de utilização de combustiveis \033[31m{combustivel:.2f} tonCO2\033[m por ano, totalizando "
      f"até agora \033[31m{carbonoTotal:.2f}\033[m tonCO2 por ano!")
print()
dinheiroEnergia = float(input('Qual o valor médio mensal da conta de energia elétrica de sua empresa?: R$'))
tipoEnergia = int(input(
    'Sua empresa faz uso de energia solar?\nUse \033[1;31m1 = Não, \033[1;32m2 = Sim, compro a minha energia de uma '
    'fazenda solar, \033[1;33m3 = Sim, além de consumir da rede, faço geração própria\033[m :'))
while (tipoEnergia > 3) or (tipoEnergia < 1):
    print()
    print("Opção inválida!\n \033[1;31mTENTE NOVAMENTE!\033[m")
    print()
    tipoEnergia = int(input(
        'Sua empresa faz uso de energia solar?\nUse \033[1;31m1 = Não, \033[1;32m2 = Sim, compro a minha energia de uma'
        ' fazenda solar, \033[1;33m3 = Sim, além de consumir da rede, faço geração própria\033[m :'))
if tipoEnergia == 1:
    energia = dinheiroEnergia * 0.002136
    carbonoTotal += energia
elif tipoEnergia == 2:
    energia = dinheiroEnergia * 0.000816
    carbonoTotal += energia
elif tipoEnergia == 3:
    energia = dinheiroEnergia * 0.004164
    carbonoTotal += energia
print()
print(f"Você emite por meio de utilização de energia \033[31m{energia:.2f} tonCO2\033[m por ano, totalizando até agora "
     f"\033[31m{carbonoTotal:.2f} tonCO2\033[m por ano!")
print()
vendasMês = int(input('Quantas vendas com frete a sua empresa faz por mês?: '))
local = int(input('Onde estão localizados a maioria da sua clientela?\nUse \033[1;31m1 = até 50 km distante, '
                  '\033[1;32m2 = 50km a 300 km, \033[1;33m3 = 300km a 1000 km, \033[1;34m4 = 1000km a 2000 km\033[m: '))
print()
while (local > 4) or (local < 1):
    print()
    print("Opção inválida!\n \033[1;31mTENTE NOVAMENTE!\033[m")
    print()
    local = int(input('Onde estão localizados a maioria da sua clientela?:\nUse \033[1;31m1 = até 50 km distante, '
                      '\033[1;32m2 = 50km a 300 km, \033[1;33m3 = 300km a 1000 km, \033[1;34m4 = 1000km a 2000 km\033[m: '))
if local == 1:
    frete = vendasMês * 0.002136
    carbonoTotal += frete
elif local == 2:
    frete = vendasMês * 0.000816
    carbonoTotal += frete
elif local == 3:
    frete = vendasMês * 0.004164
    carbonoTotal += frete
elif local == 4:
    frete = vendasMês * 0.004164
    carbonoTotal += frete
print(f"Você emite por meio de utilização de frete \033[31m{frete:.2f} tonCO2\033[m por ano, totalizando até agora "
     f"\033[31m{carbonoTotal:.2f} tonCO2\033[m por ano!")
print()

arvoresPlantadas = int(input('Quantas árvores sua empresa planta por ano?: '))
print()
metaArvores = math.ceil(carbonoTotal)*7
credito = 0
if arvoresPlantadas > metaArvores:
    for i in range(metaArvores, arvoresPlantadas):
        credito += 950.00
    print(f"Você plantou {arvoresPlantadas}/{metaArvores} da sua meta para compensar o carbono emitido pela empresa"
          f" \033[1;32m{empresa}\033[m, \033[32me recebe um crédito de R${credito:.2f} por isso :)\033[m")
elif arvoresPlantadas == metaArvores:
    print(f"Você plantou {arvoresPlantadas}/{metaArvores} da sua meta para compensar o carbono emitido pela empresa"
          f" \033[1;32m{empresa}\033[m")
else:
    print(f"Você plantou {arvoresPlantadas}/{metaArvores} da sua meta para compensar o carbono emitido pela empresa"
          f" \033[1;32m{empresa}\033[m, \033[31mnão bateu a quantidade nescessária de arvores plantadas :(\033[m")
