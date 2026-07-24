from cryptography.fernet import Fernet
import json
import pyperclip
import lib.interface
import lib.funções

while True:
    resposta = lib.interface.menu(["Adicionar Senha", "Ver senhas salvas", "Procurar senha", "Sair"])
    if resposta == 1:
        lib.funções.adicionarSenha()

    elif resposta == 2:
        a = lib.funções.verSenhas()
        print(a)

    elif resposta == 3:
        lib.funções.procurarSenha()

    elif resposta == 4:
        print("Obrigado por usar esse sistema")
        break

    else:
        print("Digitre algo válido!")