import lib.interface
import lib.funções

while True:
    resposta = lib.interface.menu(["Adicionar Senha", "Ver senhas salvas", "Procurar senha", "Sair"])
    if resposta == 1:
        lib.funções.adicionarSenha()

    elif resposta == 2:
        lib.funções.verSenhas()
        x = input("\nPressione ENTER para voltar ao menu!")

    elif resposta == 3:
        lib.funções.procurarSenha()

    elif resposta == 4:
        print("Obrigado por usar esse sistema")
        break

    else:
        print("Digitre algo válido!")