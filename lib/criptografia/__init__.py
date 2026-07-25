from cryptography.fernet import Fernet
import os


def gerarKey():
    if not os.path.exists('key.key'):
        key = Fernet.generate_key()
       
        with open('key.key', 'wb') as arquivo:
            arquivo.write(key)
            return key
    else:
        print("Arquivo já existe")
    

def carregarKey():
    if not os.path.exists("key.key"):
        chave = gerarKey()
        return chave

    else:
        with open('key.key', 'rb') as arquivo:
            chave_lida = arquivo.read()
        return chave_lida

def criptografar(texto):
    key = carregarKey()
    fernet = Fernet(key)
    token = fernet.encrypt(texto.encode())
    token = token.decode()
    return token




def descriptografar(token):
    key = carregarKey()
    fernet = Fernet(key)
    texto = fernet.decrypt(token.encode())
    texto = texto.decode()
    return texto