from tkinter import *


def toEnter():
    titulo['text'] = " "
    subtitulo['text'] = "Logado"

    print("Nome usuário: %s" % primeiroNomeUser.get())


sistemaLogin = Tk()


# Definições do app

sistemaLogin.title("Gerenciador de login e cadastro")
sistemaLogin.geometry("900x500")
sistemaLogin.configure(background="#f2f2f2")

# Definições da tela do usuário

titulo = Label(sistemaLogin, text="Automation Practice", font="Tahoma 25")
titulo.place(x=300, y=70)

subtitulo = Label(sistemaLogin, text="t", font="Tahoma 25")
subtitulo.place(x=370, y=70)

email = Label(sistemaLogin, text="Digite seu email", font="Tahoma 10")
email.place(x=100, y=150)

primeiroNome = Label(sistemaLogin, text="Digite seu nome", font="Tahoma 10")
primeiroNome.place(x=100, y=210)

segundoNome = Label(
    sistemaLogin, text="Digite seu sobrenome", font="Tahoma 10")
segundoNome.place(x=100, y=270)

senha = Label(sistemaLogin, text="Digite uma senha", font="Tahoma 10")
senha.place(x=100, y=330)

diaNasc = Label(sistemaLogin, text="Dia", font="Tahoma 10")
mesNasc = Label(sistemaLogin, text="Mes", font="Tahoma 10")
anoNasc = Label(sistemaLogin, text="Ano", font="Tahoma 10")

diaNasc.place(x=100, y=370)
mesNasc.place(x=130, y=370)
anoNasc.place(x=200, y=370)

nomeEmpresa = Label(sistemaLogin, text="Nome da sua empresa", font="Tahoma 10")
nomeEmpresa.place(x=400, y=150)

cidade = Label(sistemaLogin, text="Sua cidade", font="Tahoma 10")
cidade.place(x=400, y=210)

endUm = Label(sistemaLogin, text="Digite o primeiro endereço",
              font="Tahoma 10")
endDois = Label(sistemaLogin, text="Digite o segundo endereço",
                font="Tahoma 10")

endUm.place(x=400, y=270)
endDois.place(x=400, y=330)

cep = Label(sistemaLogin, text="Digite seu cep", font="Tahoma 10")
cep.place(x=650, y=150)

estado = Label(sistemaLogin, text="Digite seu estado", font="Tahoma 10")
estado.place(x=650, y=210)

tel = Label(sistemaLogin, text="Digite seu telefone", font="Tahoma 10")
tel.place(x=650, y=270)

celular = Label(sistemaLogin, text="Digite seu celular", font="Tahoma 10")
celular.place(x=650, y=330)

# Definições da entrada de dados

email = Entry(sistemaLogin)
email.place(x=100, y=170, width=200)

primeiroNomeEnter = Entry(sistemaLogin)
primeiroNomeEnter.place(x=100, y=230)

segundoNomeEnter = Entry(sistemaLogin)
segundoNomeEnter.place(x=100, y=290)

senhaEnter = Entry(sistemaLogin, show='*')
senhaEnter.place(x=100, y=350)

diaNascEnter = Entry(sistemaLogin)
diaNascEnter.place(x=100, y=390, width=25)

mesNascEnter = Entry(sistemaLogin)
mesNascEnter.place(x=130, y=390, width=60)

anoNascEnter = Entry(sistemaLogin)
anoNascEnter.place(x=200, y=390, width=40)

nomeEmpresaEnter = Entry(sistemaLogin)
nomeEmpresaEnter.place(x=400, y=170)

cidadeEnter = Entry(sistemaLogin)
cidadeEnter.place(x=400, y=230)

endUmEnter = Entry(sistemaLogin)
endUmEnter.place(x=400, y=290, width=160)

endDoisEnter = Entry(sistemaLogin)
endDoisEnter.place(x=400, y=350, width=160)

cepEnter = Entry(sistemaLogin)
cepEnter.place(x=650, y=170)

estadoEnter = Entry(sistemaLogin)
estadoEnter.place(x=650, y=230)

telEnter = Entry(sistemaLogin)
telEnter.place(x=650, y=290)

celEnter = Entry(sistemaLogin)
celEnter.place(x=650, y=350)

botao_enviar = Button(sistemaLogin, width=25, text="Enviar", command=toEnter)
botao_enviar.place(x=330, y=450)


sistemaLogin.mainloop()
