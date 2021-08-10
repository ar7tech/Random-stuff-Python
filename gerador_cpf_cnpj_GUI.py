# Versão 1.0.0
# 13/12/2020

from tkinter import Frame, Pack, Label, Entry, Button, LEFT, Tk, Text
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
        n_cpf[a] = n_cpf[a] * multiplo
        res_dv = res_dv + n_cpf[a]
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

def CalcularDigitosCnpj(numeros):
    if len(numeros) == 12:
        qnt = len(numeros) - 4
    else:
        qnt = len(numeros) - 5
    multiplo = 2
    res_dv = 0
    n_cnpj = numeros[::-1]
    for c in range(qnt):
        n_cnpj[c] = n_cnpj[c] * multiplo
        res_dv = res_dv + n_cnpj[c]
        multiplo = multiplo + 1
    qnt = len(n_cnpj)
    multiplo = 2
    for d in range(8, qnt):
        n_cnpj[d] = n_cnpj[d] * multiplo
        res_dv = res_dv + n_cnpj[d]
        multiplo = multiplo + 1
    dv = 11-(res_dv % 11)
    return ValidaDigito(dv)

def FormatarCnpj(num_cnpj):
    teste = num_cnpj
    qnt = len(num_cnpj)
    for b in range(qnt):
        if b == 1 or b == 5:
            teste[b] = str(teste[b]) + '.'
        elif b == 7:
            teste[b] = str(teste[b]) + '/'
        elif b == 11:
            teste[b] = str(teste[b]) + '-'
    return teste

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.w01Container = Frame(master)
        self.w01Container["pady"] = 10
        self.w01Container.pack()

        self.w02Container = Frame(master)
        self.w02Container["padx"] = 20
        self.w02Container.pack()

        self.w03Container = Frame(master)
        self.w03Container["padx"] = 20
        self.w03Container.pack()

        self.w99Container = Frame(master)
        self.w99Container["pady"] = 20
        self.w99Container.pack()
###############################################################################################################################################################
        self.titulo01 = Label(self.w01Container, text="Gerador de documentos (CPF/CNPJ)")
        self.titulo01["font"] = ("Arial", "20", "bold")
        self.titulo01.pack()
###############################################################################################################################################################
        self.titulo02 = Label(self.w02Container, text="Formatação")
        self.titulo02["font"] = ("Arial", "10", "bold")
        self.titulo02.pack()

        self.campo01Label = Label(self.w02Container,text="S/N:", font=self.fontePadrao)
        self.campo01Label.pack(side=LEFT)
        self.campo01 = Entry(self.w02Container)
        self.campo01["width"] = 2
        self.campo01["font"] = self.fontePadrao
        self.campo01.pack(side=LEFT)
###############################################################################################################################################################
        self.cpfLabel = Label(self.w03Container,text="CPF:", font=self.fontePadrao)
        self.cpfLabel.pack(side=LEFT)
        self.cpf = Label(self.w03Container, text="", font=self.fontePadrao)
        self.cpf.pack(side=LEFT)

        self.cnpjLabel = Label(self.w03Container,text="CNPJ:", font=self.fontePadrao)
        self.cnpjLabel.pack(side=LEFT)
        self.cnpj = Label(self.w03Container, text="", font=self.fontePadrao)
        self.cnpj.pack(side=LEFT)
###############################################################################################################################################################
        self.gerarcpf = Button(self.w99Container)
        self.gerarcpf["text"] = "CPF"
        self.gerarcpf["font"] = ("Calibri", "8")
        self.gerarcpf["width"] = 12
        self.gerarcpf["command"] = self.GerarCPF
        self.gerarcpf.pack(side=LEFT)

        self.gerarcnpj = Button(self.w99Container)
        self.gerarcnpj["text"] = "CNPJ"
        self.gerarcnpj["font"] = ("Calibri", "8")
        self.gerarcnpj["width"] = 12
        self.gerarcnpj["command"] = self.GerarCNPJ
        self.gerarcnpj.pack(side=LEFT)
###############################################################################################################################################################
    def GerarCPF(self):
        gerar_numero_cpf = [0] * 9
        gerar_numero_cpf = GerarNumeros(gerar_numero_cpf)
        cpf_dv_1 = CalcularDigitosCpf(gerar_numero_cpf.copy())
        gerar_numero_cpf.append(cpf_dv_1)
        cpf_dv_2 = CalcularDigitosCpf(gerar_numero_cpf.copy())
        gerar_numero_cpf.append(cpf_dv_2)
        if self.campo01.get().upper() == 'S':
            gerar_numero_cpf = FormatarCpf(gerar_numero_cpf)
            teste = ''.join(str(a) for a in gerar_numero_cpf)
            self.cpf["text"] = teste
        elif self.campo01.get().upper() == 'N':
            teste = ''.join(str(a) for a in gerar_numero_cpf)
            self.cpf["text"] = teste
        else:
            self.cpf["text"] = 'Opção incorreta!'

    def GerarCNPJ(self):
        gerar_numero_cnpj = [0] * 12
        gerar_numero_cnpj = GerarNumeros(gerar_numero_cnpj)
        cnpj_dv_1 = CalcularDigitosCnpj(gerar_numero_cnpj.copy())
        gerar_numero_cnpj.append(cnpj_dv_1)
        cnpj_dv_2 = CalcularDigitosCnpj(gerar_numero_cnpj.copy())
        gerar_numero_cnpj.append(cnpj_dv_2)
        if self.campo01.get().upper() == 'S':
            gerar_numero_cnpj = FormatarCnpj(gerar_numero_cnpj)
            teste = ''.join(str(a) for a in gerar_numero_cnpj)
            self.cnpj["text"] = teste
        elif self.campo01.get().upper() == 'N':
            teste = ''.join(str(a) for a in gerar_numero_cnpj)
            self.cnpj["text"] = teste
        else:
            self.cnpj["text"] = 'Opção incorreta!'

root = Tk()
Application(root)
root.mainloop()