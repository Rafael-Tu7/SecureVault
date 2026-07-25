import json
import pyperclip
import json
import lib.interface
from lib.criptografia import criptografar, descriptografar

def adicionarSenha():
    lib.interface.cabeçalho("Adicionar senha")
    lib.interface.linha()
    print("")
    servico = lib.interface.leiaEntrada("Digite o nome do serviço: ")
    usuario = lib.interface.leiaEntrada("Digite o seu usuário: ")
    senha = criptografar(lib.interface.leiaEntrada("Digite sua senha: "))

    senhas_usuario = {
        "usuario": usuario,
        "senha": senha
    }

    try:
         with open('dados.json', 'r', encoding='utf-8') as arquivo:
              lista_senhas = json.load(arquivo)
    except FileNotFoundError:
         lista_senhas = {}

    # Adicionar novos dados
    lista_senhas[servico] = senhas_usuario

    # Salvar lista atualizada
    with open('dados.json', 'w') as arquivo:
         json.dump(lista_senhas, arquivo, indent=4)



def verSenhas():
    try:
        with open('dados.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print("Erro ao encontrar arquivo!")
    else:
        if not dados:
             print("Nenhuma senha foi registrada!")
             return

        lib.interface.cabeçalho("Suas senhas")
        id = 1
        for servico, info in dados.items():
            lib.interface.linha()
            print(f"ID = {id}")
            print(f"Serviço: {servico}")
            print(f"Usuário: {info['usuario']}")
            print(f"Senha: {descriptografar(info['senha'])}")
            id += 1
            lib.interface.linha()
        

def procurarSenha():

    try:
        with open('dados.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print("Erro ao encontrar o arquivo!")
    else:
        if not dados:
            print("Nenhuma senha foi registrada!")
            return
        
        else: 
            lib.interface.linha()
            lib.interface.cabeçalho("Procure sua senha!")
            lib.interface.linha()

            senha_procurada = lib.interface.leiaEntrada("Digite o serviço que está procurando sua senha: ")
            
            for servico, info in dados.items():
                        if servico == senha_procurada:
                            lib.interface.linha()                   
                            print(f"Serviço: {servico}")
                            print(f"Usuário: {info['usuario']}")
                            print(f"Senha: {descriptografar(info['senha'])}")
                            lib.interface.linha()
                            break
            else:
                print("Erro ao encontrar serviço!")


#def bloquearSistema():
     