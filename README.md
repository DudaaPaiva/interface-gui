# Sistema de Login e Cadastro com PySimpleGUI e SQLite

Este projeto é um sistema de **login e cadastro de usuários** utilizando **PySimpleGUI** para a interface gráfica e **SQLite** como banco de dados.

## Funcionalidades

- **Login**: Autenticação de usuários com nome de usuário e senha.
- **Cadastro**: Registro de novos usuários.
- **Boas-vindas**: Tela exibida após login bem-sucedido.

## Tecnologias

- **Python**
- **PySimpleGUI**
- **SQLite**

## Banco de Dados

O banco de dados **usuarios.db** é usado para armazenar as credenciais dos usuários com a seguinte estrutura:

sql
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
);

## Melhorias Futuras

- **Criptografar Senhas**
- **Validação de Senha**
- **Interface Melhorada**

