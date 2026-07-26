# SecureVault

O SecureVault é um projeto desenvolvido em Python com o objetivo de estudar programação, organização de código e conceitos básicos de segurança da informação. A ideia do projeto é criar um gerenciador de senhas simples, permitindo armazenar credenciais de diferentes serviços de forma segura.

O projeto foi desenvolvido de forma modular, facilitando a manutenção e a adição de novas funcionalidades ao longo do desenvolvimento.

## Funcionalidades

Atualmente o SecureVault possui as seguintes funcionalidades:

* Cadastro de novas senhas;
* Visualização das senhas cadastradas;
* Pesquisa de senhas por serviço;
* Criptografia das senhas utilizando Fernet;
* Descriptografia automática ao visualizar ou pesquisar uma senha;
* Geração automática da chave de criptografia;
* Sistema de autenticação por senha mestra;
* Armazenamento da senha mestra utilizando hash com bcrypt;
* Bloqueio e desbloqueio do cofre;
* Tratamento para arquivos inexistentes e cofre vazio.

## Tecnologias utilizadas

* Python 3
* Cryptography (Fernet)
* bcrypt
* JSON

## Estrutura do projeto

```text
SecureVault/
│
├── main.py
├── .gitignore
├── dados.json
├── key.key
├── auth.dat
│
└── lib/
    ├── interface/
    ├── funções/
    ├── criptografia/
```

## Segurança

As senhas cadastradas não são armazenadas em texto puro. Cada senha é criptografada utilizando o algoritmo Fernet antes de ser salva no arquivo de dados.

A senha mestra utiliza bcrypt, sendo armazenado apenas seu hash. Dessa forma, a senha original nunca fica salva no computador e apenas sua verificação é realizada durante o desbloqueio do cofre.

Os arquivos que contêm informações sensíveis (`dados.json`, `key.key` e `auth.dat`) estão incluídos no `.gitignore` e não são enviados para o repositório no GitHub.

## Próximas funcionalidades

Algumas melhorias previstas para as próximas versões são:

* edição de senhas;
* exclusão de senhas;
* gerador de senhas seguras;
* organização por categorias;
* favoritos;
* interface gráfica.

## Objetivo

Este projeto foi criado com o objetivo de praticar conceitos de programação em Python, como modularização, manipulação de arquivos, criptografia, hash de senhas, tratamento de exceções e utilização do Git e GitHub.

Todo o desenvolvimento foi feito de forma incremental, adicionando novas funcionalidades e melhorando a estrutura do projeto a cada versão.
