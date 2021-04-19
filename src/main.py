# -*- coding: utf-8 -*-

from tkinter import *


def toEnter():
    nomeEmpresa["text"] = "Logado"


sistemaLogin = Tk()

nomeEmpresa = Label(sistemaLogin, text="Mercado Eletrônico", font="Tahoma 25")
nomeEmpresa.place(x=250, y=100)

botao_logar = Button(sistemaLogin, width=25, text="Logar", command=toEnter)
botao_logar.place(x=300, y=400)

sistemaLogin.geometry("800x600+0+0")
sistemaLogin.mainloop()
