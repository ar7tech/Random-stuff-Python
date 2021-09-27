# Versão 2.0.0
# Criado em: 13/12/2020
# Alterado em: 22/08/2021

from random import randint

def GerarNumeros(gerar):
    qnt = len(gerar)
    for x in range(qnt):
        gerar[x] = randint(0, 9)
    return gerar

def ValidaDigito(dv):
    if dv >= 10:
        dv = 0
        return dv
    else:
        return dv

def CalcularDigitosCpf(n_cpf):
    qnt = len(n_cpf)
    multiplo = qnt + 1
    res_dv = 0
    for a in range(qnt):
        n_cpf[a] = int(n_cpf[a]) * multiplo
        res_dv = res_dv + int(n_cpf[a])
        multiplo = multiplo - 1
    dv = 11-(res_dv % 11)
    return ValidaDigito(dv)

def FormatarCpf(num_cpf):
    teste = num_cpf
    qnt = len(num_cpf)
    for b in range(qnt):
        if b == 2 or b == 5:
            teste[b] = str(teste[b]) + '.'
        elif b == 8:
            teste[b] = str(teste[b]) + '-'
    return teste

def GerarCPF(formata):
    gerar_numero_cpf = [0] * 9
    gerar_numero_cpf = GerarNumeros(gerar_numero_cpf)
    cpf_dv_1 = CalcularDigitosCpf(gerar_numero_cpf.copy())
    gerar_numero_cpf.append(cpf_dv_1)
    cpf_dv_2 = CalcularDigitosCpf(gerar_numero_cpf.copy())
    gerar_numero_cpf.append(cpf_dv_2)
    if formata == 'S':
        gerar_numero_cpf = FormatarCpf(gerar_numero_cpf)
        teste = ''.join(str(a) for a in gerar_numero_cpf)
        return teste
    elif formata == 'N':
        teste = ''.join(str(a) for a in gerar_numero_cpf)
        return teste
    else:
        return 'Opção incorreta!'

def ValidaCPF(n_cpf):
    resto_cpf = n_cpf[0:9]
    gerar_numero_cpf = list(resto_cpf)
    cpf_dv_1 = CalcularDigitosCpf(gerar_numero_cpf.copy())
    gerar_numero_cpf.append(cpf_dv_1)
    cpf_dv_2 = CalcularDigitosCpf(gerar_numero_cpf.copy())
    gerar_numero_cpf.append(cpf_dv_2)
    resultado = ''.join(str(a) for a in gerar_numero_cpf)
    if n_cpf == resultado:
        return print('CPF Verdadeiro!')
    else:
        return print(f'CPF Falso, o CPF correto é: ', resultado)

def CalcularDigitosCnpj(numeros):
    if len(numeros) == 12:
        qnt = len(numeros) - 4
    else:
        qnt = len(numeros) - 5
    multiplo = 2
    res_dv = 0
    n_cnpj = numeros[::-1]
    for c in range(qnt):
        n_cnpj[c] = int(n_cnpj[c]) * multiplo
        res_dv = res_dv + int(n_cnpj[c])
        multiplo = multiplo + 1
    qnt = len(n_cnpj)
    multiplo = 2
    for d in range(8, qnt):
        n_cnpj[d] = int(n_cnpj[d]) * multiplo
        res_dv = res_dv + int(n_cnpj[d])
        multiplo = multiplo + 1
    dv = 11-(res_dv % 11)
    return ValidaDigito(dv)

def FormatarCnpj(num_cnpj):
    teste = num_cnpj
    qnt = len(num_cnpj)
    for b in range(qnt):
        if b == 1 or b == 4:
            teste[b] = str(teste[b]) + '.'
        elif b == 7:
            teste[b] = str(teste[b]) + '/'
        elif b == 11:
            teste[b] = str(teste[b]) + '-'
    return teste

def GerarCNPJ(formata):
    gerar_numero_cnpj = [0] * 12
    gerar_numero_cnpj = GerarNumeros(gerar_numero_cnpj)
    cnpj_dv_1 = CalcularDigitosCnpj(gerar_numero_cnpj.copy())
    gerar_numero_cnpj.append(cnpj_dv_1)
    cnpj_dv_2 = CalcularDigitosCnpj(gerar_numero_cnpj.copy())
    gerar_numero_cnpj.append(cnpj_dv_2)
    if formata == 'S':
        gerar_numero_cnpj = FormatarCnpj(gerar_numero_cnpj)
        teste = ''.join(str(a) for a in gerar_numero_cnpj)
        return teste
    elif formata == 'N':
        teste = ''.join(str(a) for a in gerar_numero_cnpj)
        return teste
    else:
        return 'Opção incorreta!'

def ValidaCNPJ(n_cnpj):
    resto_cnpj = n_cnpj[0:12]
    gerar_numero_cnpj = list(resto_cnpj)
    cnpj_dv_1 = CalcularDigitosCnpj(gerar_numero_cnpj.copy())
    gerar_numero_cnpj.append(cnpj_dv_1)
    cnpj_dv_2 = CalcularDigitosCnpj(gerar_numero_cnpj.copy())
    gerar_numero_cnpj.append(cnpj_dv_2)
    resultado = ''.join(str(a) for a in gerar_numero_cnpj)
    if n_cnpj == resultado:
        return print('CNPJ Verdadeiro!')
    else:
        return print(f'CNPJ Falso, o CNPJ correto é: ', resultado)

print(GerarCPF('S'))

print(GerarCNPJ('S'))

verificar_cpf = ValidaCPF(input('Digite o CPF para validação: '))

verificar_cnpj = ValidaCNPJ(input('Digite o CNPJ para validação: '))
