# Teste
# import math
from math import pow
# hoje = datetime.now().strftime('%d/%m/%Y')

# Funcao para calcular rendimento total com base em percentual mensal ao longo de X anos.
def CalculaRendimentoAno(perc_mes, anos):
    rend_no_ano = ((((perc_mes/100) + 1) ** 12) - 1) * 100
    rend_anos = ((((rend_no_ano/100) + 1) ** anos) - 1) * 100
    # return rend_no_ano, rend_anos
    return "Rendimento no ano: " + str(round(rend_no_ano, 2)) + "%\n" + "Rendimento para " + str(anos) + " anos: " + str(round(rend_anos, 2)) + "%"

teste = CalculaRendimentoAno(0.56, 3)

# print(teste)

# Funcao para calcular rendimento mensal com base em percentual total de x anos.
def CalculaRendimentoMes(perc_ano, anos):
    rend_mes_ano = (pow(((perc_ano/100) + 1), 1/12) - 1) * 100
    rend_mes = (pow(((rend_mes_ano/100) + 1), 1/anos) - 1) * 100
    # return rend_mes
    return f"Rendimento ao mes: {round(rend_mes, 4)}%"

teste2 = CalculaRendimentoMes(7, 1)

# print(teste2)

def CalculaRendimentoReal(perc_ano, infla_ano):
    res = ((1+(perc_ano/100))/(1+(infla_ano/100))-1)*100
    # return res
    return f"Rendimento real: %.4f" %res + "%"

teste3 = CalculaRendimentoReal(10, 5)

# print(teste3)

def calculaInvestimentoFinal():
    val_inicial = float(input("Informe o aporte inicial: "))
    val_mes = float(input("Informe o aporte mensal: "))
    perc_ano = float(input("Informe o percentual por ano: "))
    qnt_anos = int(input("Informe o periodo em anos: "))
    total = 0
    qnt_meses = qnt_anos * 12
    perc_mes = (((perc_ano / 100) + 1) ** (1/12)) - 1

    for x in range(qnt_meses):
        if x == 0:
            total += val_inicial * (1 + perc_mes)
        else:
            total = (total + val_mes) * (1 + perc_mes)
    print(f"Efetuando um aporte inicial de R${val_inicial}, com aportes mensais de R${val_mes}, por um periodo de {qnt_anos} ano(s) e com rendimento anual de {perc_ano}%, terá o valor acumulado de R${round(total, 2)}")

calculaInvestimentoFinal()
