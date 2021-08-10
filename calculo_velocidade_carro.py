# Versão 1.0.0
# 19/10/2020

def menu():
    print('Iniciar calculo, digite "1"')
    print('Sair do programa, digite "0"')

def calculo():
    print('---------------------------------------------------------------------------')
    print('Informe as dimensoes do Pneu a seguir!')
    print('')
    medida_1 = float(input('Tamanho: '))
    medida_2 = float(input('Proporcao: '))
    medida_3 = float(input('Aro: '))
    calc_pneu = ((((medida_1 * (medida_2 / 100)) / 10) * 2 + (medida_3 * 2.54)) * 3.1415) / 100
    print('Circunferencia do Pneu: ', str(round(calc_pneu, 3)) + 'm')
    print('')
    print('---------------------------------------------------------------------------')
    print('')
    print('Informe os dados referentes as caracteristicas mecanicas do carro a seguir!')
    print('')
    diferencial = float(input('Relacao do diferencial: '))
    rel_marcha = float(input('Relacao da marcha: '))
    rpm_motor = float(input('Rotacao do motor em RPM: '))
    calc_reducao = ((rpm_motor / rel_marcha) / diferencial) / 60
    calc_vel_final = (calc_reducao * calc_pneu) * 3.6
    print('Velocidade maxima teorica: ', str(round(calc_vel_final, 2)) + 'Km/H')

menu()
opcao = int(input('Escolha uma opcao: '))

while opcao != 0:
    if opcao == 1:
        calculo()
    else:
        print('Opcao invalida, tente novamente.')
    print()
    menu()
    opcao = int(input('Escolha uma opcao: '))

print('Obrigado por usar o programa!')
