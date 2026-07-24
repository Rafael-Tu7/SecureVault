def linha(tam=40):
    print("=" * tam)

def cabeçalho(txt):
    linha()
    print(txt.center(40))
    linha()


def menu(lst):
    cabeçalho("SecureVault")
    c = 1
    for aba in lst:
        print(f"{c} - {aba}")
        c +=1
    linha()
    opc = leiaOpc("Digite o menu que deseja acessar: ")
    return opc



def leiaOpc(msg):
    try:
        n = int(input(msg))
    except (TypeError, ValueError):
        print("Digite uma opção válida!")
        
    except KeyboardInterrupt:
        print("O usuário preferiu não digitar")
        return 0
    else:
        return n


def leiaEntrada(msg):
    try:
        entrada = str(input(msg))
    except (TypeError, ValueError):
        print("Digite uma opção válida!")
            
    except KeyboardInterrupt:
        print("O usuário preferiu não digitar")
    else:
        return entrada