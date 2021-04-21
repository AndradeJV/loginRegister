from tkinter import *


def toEnter():
    tituloInicial['text'] = "usuario logado"


def toEnterNew():
    subtitulo['text'] = "usuario cadastrado"


def toRegister():

    sistemaLogin = Tk()

    sistemaLogin.title("Gerenciador de login e cadastro")

    sistemaLogin.geometry("900x500")
    sistemaLogin.configure(background="#f2f2f2")

    titulo = Label(sistemaLogin, text="Automation Practice", font="Tahoma 25")
    titulo.place(x=300, y=70)

    subtitulo = Label(sistemaLogin, text="t", font="Tahoma 25")
    subtitulo.place(x=370, y=70)

    email = Label(sistemaLogin, text="Digite seu email", font="Tahoma 10")
    email.place(x=100, y=150)
    emailEnter = Entry(sistemaLogin)
    emailEnter.place(x=100, y=170, width=200)

    primeiroNome = Label(
        sistemaLogin, text="Digite seu nome", font="Tahoma 10")
    primeiroNome.place(x=100, y=210)
    primeiroNomeEnter = Entry(sistemaLogin)
    primeiroNomeEnter.place(x=100, y=230)

    primeiroNome = Label(
        sistemaLogin, text="Digite seu nome", font="Tahoma 10")
    primeiroNome.place(x=100, y=210)
    primeiroNomeEnter = Entry(sistemaLogin)
    primeiroNomeEnter.place(x=100, y=230)

    segundoNome = Label(
        sistemaLogin, text="Digite seu sobrenome", font="Tahoma 10")
    segundoNome.place(x=100, y=270)
    segundoNomeEnter = Entry(sistemaLogin)
    segundoNomeEnter.place(x=100, y=290)

    senha = Label(sistemaLogin, text="Digite uma senha", font="Tahoma 10")
    senha.place(x=100, y=330)
    senhaEnter = Entry(sistemaLogin, show='*')
    senhaEnter.place(x=100, y=350)

    diaNasc = Label(sistemaLogin, text="Dia", font="Tahoma 10")
    diaNasc.place(x=100, y=370)
    diaNascEnter = Entry(sistemaLogin)
    diaNascEnter.place(x=100, y=390, width=25)

    mesNasc = Label(sistemaLogin, text="Mes", font="Tahoma 10")
    mesNasc.place(x=130, y=370)
    mesNascEnter = Entry(sistemaLogin)
    mesNascEnter.place(x=130, y=390, width=60)

    anoNasc = Label(sistemaLogin, text="Ano", font="Tahoma 10")
    anoNasc.place(x=200, y=370)
    anoNascEnter = Entry(sistemaLogin)
    anoNascEnter.place(x=200, y=390, width=40)

    nomeEmpresa = Label(
        sistemaLogin, text="Nome da sua empresa", font="Tahoma 10")
    nomeEmpresa.place(x=400, y=150)
    nomeEmpresaEnter = Entry(sistemaLogin)
    nomeEmpresaEnter.place(x=400, y=170)

    cidade = Label(sistemaLogin, text="Sua cidade", font="Tahoma 10")
    cidade.place(x=400, y=210)
    cidadeEnter = Entry(sistemaLogin)
    cidadeEnter.place(x=400, y=230)

    endUm = Label(
        sistemaLogin, text="Digite o primeiro endereço", font="Tahoma 10")
    endUm.place(x=400, y=270)
    endUmEnter = Entry(sistemaLogin)
    endUmEnter.place(x=400, y=290, width=160)

    endDois = Label(
        sistemaLogin, text="Digite o segundo endereço", font="Tahoma 10")
    endDois.place(x=400, y=330)
    endDoisEnter = Entry(sistemaLogin)
    endDoisEnter.place(x=400, y=350, width=160)

    cep = Label(sistemaLogin, text="Digite seu cep", font="Tahoma 10")
    cep.place(x=650, y=150)
    cepEnter = Entry(sistemaLogin)
    cepEnter.place(x=650, y=170)

    estado = Label(sistemaLogin, text="Digite seu estado", font="Tahoma 10")
    estado.place(x=650, y=210)
    estadoEnter = Entry(sistemaLogin)
    estadoEnter.place(x=650, y=230)

    tel = Label(sistemaLogin, text="Digite seu telefone", font="Tahoma 10")
    tel.place(x=650, y=270)
    telEnter = Entry(sistemaLogin)
    telEnter.place(x=650, y=290)

    celular = Label(sistemaLogin, text="Digite seu celular", font="Tahoma 10")
    celular.place(x=650, y=330)
    celEnter = Entry(sistemaLogin)
    celEnter.place(x=650, y=350)

    botao_enviar = Button(sistemaLogin, width=25,
                          text="Enviar", command=toEnterNew)
    botao_enviar.place(x=330, y=450)

    sistemaLogin.mainloop()


app = Tk()

app.title("Gerenciador de login e cadastro")

app.geometry("900x500")
app.configure(background="#f2f2f2")

tituloInicial = Label(
    app, text="Automation Practice", font="Tahoma 25")
tituloInicial.place(x=300, y=70)

emailLogin = Label(app, text="Digite seu email", font="Tahoma 10")
emailLogin.place(x=400, y=170)
emailLoginEnter = Entry(app)
emailLoginEnter.place(x=350, y=190, width=200)

senhaLogin = Label(app, text="Digite sua senha", font="Tahoma 10")
senhaLogin.place(x=400, y=220)
senhaLoginEnter = Entry(app, show="*")
senhaLoginEnter.place(x=350, y=240, width=200)

logar = Button(app, width=25, text="Entrar", command=toEnter)
logar.place(x=350, y=300)

novoUser = Button(app, width=25, text="Novo cadastro", command=toRegister)
novoUser.place(x=350, y=340)

app.mainloop()
