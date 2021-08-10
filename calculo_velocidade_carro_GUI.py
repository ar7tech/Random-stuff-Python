# Versão 1.0.0
# 06/12/2020

from tkinter import Frame, Pack, Label, Entry, Button, LEFT, Tk

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

        self.w04Container = Frame(master)
        self.w04Container["padx"] = 20
        self.w04Container.pack()

        self.w99Container = Frame(master)
        self.w99Container["pady"] = 20
        self.w99Container.pack()
###############################################################################################################################################################
        self.titulo01 = Label(self.w01Container, text="Dados do veículo")
        self.titulo01["font"] = ("Arial", "20", "bold")
        self.titulo01.pack()
###############################################################################################################################################################
        self.titulo02 = Label(self.w02Container, text="Dimensões do pneu")
        self.titulo02["font"] = ("Arial", "10", "bold")
        self.titulo02.pack()

        self.campo01Label = Label(self.w02Container,text="Tamanho:", font=self.fontePadrao)
        self.campo01Label.pack(side=LEFT)

        self.campo01 = Entry(self.w02Container)
        self.campo01["width"] = 15
        self.campo01["font"] = self.fontePadrao
        self.campo01.pack(side=LEFT)

        self.campo02Label = Label(self.w02Container, text="Proporção:", font=self.fontePadrao)
        self.campo02Label.pack(side=LEFT)

        self.campo02 = Entry(self.w02Container)
        self.campo02["width"] = 15
        self.campo02["font"] = self.fontePadrao
        self.campo02.pack(side=LEFT)

        self.campo03Label = Label(self.w02Container,text="Aro:", font=self.fontePadrao)
        self.campo03Label.pack(side=LEFT)

        self.campo03 = Entry(self.w02Container)
        self.campo03["width"] = 15
        self.campo03["font"] = self.fontePadrao
        self.campo03.pack(side=LEFT)
###############################################################################################################################################################
        self.titulo04 = Label(self.w03Container, text="Dados mecânicos")
        self.titulo04["font"] = ("Arial", "10", "bold")
        self.titulo04.pack()

        self.campo04Label = Label(self.w03Container, text="Rel. Diferencial:", font=self.fontePadrao)
        self.campo04Label.pack(side=LEFT)

        self.campo04 = Entry(self.w03Container)
        self.campo04["width"] = 15
        self.campo04["font"] = self.fontePadrao
        self.campo04.pack(side=LEFT)

        self.campo05Label = Label(self.w03Container,text="Rel. da Marcha:", font=self.fontePadrao)
        self.campo05Label.pack(side=LEFT)

        self.campo05 = Entry(self.w03Container)
        self.campo05["width"] = 15
        self.campo05["font"] = self.fontePadrao
        self.campo05.pack(side=LEFT)

        self.campo06Label = Label(self.w03Container,text="Rotação do motor (RPM):", font=self.fontePadrao)
        self.campo06Label.pack(side=LEFT)

        self.campo06 = Entry(self.w03Container)
        self.campo06["width"] = 15
        self.campo06["font"] = self.fontePadrao
        self.campo06.pack(side=LEFT)

        self.mensagemLabel = Label(self.w04Container,text="Resultado (Km/h):", font=self.fontePadrao)
        self.mensagemLabel.pack(side=LEFT)
###############################################################################################################################################################
        self.mensagem = Label(self.w04Container, text="", font=self.fontePadrao)
        self.mensagem.pack(side=LEFT)

        self.gerararquivo = Button(self.w99Container)
        self.gerararquivo["text"] = "Calcular"
        self.gerararquivo["font"] = ("Calibri", "8")
        self.gerararquivo["width"] = 12
        self.gerararquivo["command"] = self.calculo
        self.gerararquivo.pack()
###############################################################################################################################################################
    def calculo(self):
        medida_1 = float(self.campo01.get())
        medida_2 = float(self.campo02.get())
        medida_3 = float(self.campo03.get())
        calc_pneu = ((((medida_1 * (medida_2 / 100)) / 10) * 2 + (medida_3 * 2.54)) * 3.1415) / 100

        diferencial = float(self.campo04.get())
        rel_marcha = float(self.campo05.get())
        rpm_motor = float(self.campo06.get())
        calc_reducao = ((rpm_motor / rel_marcha) / diferencial) / 60
        calc_vel_final = (calc_reducao * calc_pneu) * 3.6
        self.mensagem["text"] = str(round(calc_vel_final, 2))

root = Tk()
Application(root)
root.mainloop()
