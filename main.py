import lib.interface
import lib.funções



if not lib.funções.senhaMestraExiste():
    lib.funções.criarSenhaMestra()
else:
    # True = Desbloqueado / False = bloqueado
    while True:
        opc = lib.interface.menu(["Desbloquear Cofre", "Bloquear cofre", "Sair"])
        if opc == 1:
            estado = lib.funções.desbloquearSistema()
            if estado == True:

           
                while True:
                    resposta = lib.interface.menu(["Adicionar Senha", "Ver senhas salvas", "Procurar senha", "Editar senha", "Excluir senha", "Bloquear Sistema", "Sair"])
                    if resposta == 1:
                        lib.funções.adicionarSenha()

                    elif resposta == 2:
                        lib.funções.verSenhas()
                        x = input("\nPressione ENTER para voltar ao menu!")

                    elif resposta == 3:
                        lib.funções.procurarSenha()

                    elif resposta == 4:
                        lib.funções.editarSenha()

                    elif resposta == 5:
                        lib.funções.excluirSenha()

                    elif resposta == 6:
                       bloqueado = lib.funções.bloquearSistema()
                       if bloqueado == False:
                            print("Sistema bloqueado!")
                            break

                    elif resposta == 7:
                        print("Voltando para o menu principal...")
                        break           

                    else:
                        print("Digitre algo válido!")

            else:
                print("Cofre bloqueado!")

        elif opc == 2:
            bloquear = lib.funções.bloquearSistema()
            if bloquear == False:
                print("Cofre bloqueado!")

        elif opc == 3:
            print("Obrigado por usar esse sistema!")
            break
        else:
            print("Digite algo válido!")