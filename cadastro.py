import sqlite3
import PySimpleGUI as sg

# Função para verificar login no banco de dados
def verificar_login(usuario, senha):
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
    usuario_encontrado = cursor.fetchone()
    conexao.close()
    return usuario_encontrado is not None

# Função para verificar se o usuário já existe
def usuario_existe(usuario):
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario,))
    usuario_encontrado = cursor.fetchone()
    conexao.close()
    return usuario_encontrado is not None

# Função para cadastrar um novo usuário no banco de dados
def cadastrar_usuario(usuario, senha):
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
    conexao.commit()
    conexao.close()

# Função da tela de boas-vindas após o login
def tela_bem_vindo(usuario):
    layout = [[sg.Text(f'Bem-vindo, {usuario}!', font=('Arial', 16))],
              [sg.Button('Sair')]]
    janela = sg.Window('Painel do Usuário', layout)
    while True:
        evento, _ = janela.read()
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            break
    janela.close()

# Função da tela de cadastro de novo usuário
def tela_cadastro():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Novo Usuário', font=('Arial', 16))],
        [sg.Text('Usuário', size=(8, 1)), sg.Input(key='usuario', size=(20, 1))],
        [sg.Text('Senha', size=(8, 1)), sg.Input(key='senha', password_char='*', size=(20, 1))],
        [sg.Button('Cadastrar')]
    ]
    janela = sg.Window('Cadastro de Usuário', layout)

    while True:
        evento, valores = janela.read()
        if evento == sg.WINDOW_CLOSED:
            break
        if evento == 'Cadastrar':
            usuario = valores['usuario']
            senha = valores['senha']
            if usuario and senha:  # Verifica se o campo de usuário e senha não estão vazios
                if usuario_existe(usuario):  # Verifica se o usuário já existe
                    sg.popup('Usuário já existe! Escolha outro nome de usuário.', title='Erro')
                else:
                    cadastrar_usuario(usuario, senha)
                    sg.popup('Usuário cadastrado com sucesso!', title='Sucesso')
                    janela.close()  # Fecha a janela de cadastro
                    tela_login()  # Volta para a tela de login
            else:
                sg.popup('Preencha todos os campos!', title='Erro')

    janela.close()

# Criar a tela de login
def tela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Usuário', size=(8, 1)), sg.Input(key='usuario', size=(20, 1))],
        [sg.Text('Senha', size=(8, 1)), sg.Input(key='senha', password_char='*', size=(20, 1))],
        [sg.Button('Entrar'), sg.Button('Cadastrar')]
    ]
    janela = sg.Window('Tela de Login', layout)

    while True:
        evento, valores = janela.read()
        if evento == sg.WINDOW_CLOSED:
            break
        if evento == 'Entrar':
            usuario = valores['usuario']
            senha = valores['senha']
            if verificar_login(usuario, senha):
                sg.popup('Login bem-sucedido!', title='Sucesso')
                janela.close()  # Fecha a tela de login
                tela_bem_vindo(usuario)  # Abre a tela de boas-vindas
                tela_login()  # Volta para a tela de login quando o usuário sai
            else:
                sg.popup('Usuário ou senha incorretos!', title='Erro')
        if evento == 'Cadastrar':  # Quando o usuário clicar em 'Cadastrar'
            janela.close()  # Fecha a tela de login
            tela_cadastro()  # Abre a tela de cadastro

    janela.close()

# Executar a tela de login ao iniciar o programa
tela_login()
