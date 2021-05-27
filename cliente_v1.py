import socket
from time import sleep


def cliente():
    repeticiones = 3
    while repeticiones != 0:
        st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = 'localhost'
        port = 16033
        st.connect((host, port))
        cometido = pedir_cometido()
        preguntado = pedir_preguntado(cometido)
        st.send(bytes(preguntado, "utf-8"))
        respuesta = st.recv(128)
        print(f'Respuesta: {respuesta.decode("utf-8")}')
        st.close()
        repeticiones -= 1


# tomar variables de la entrada de usuario
def pedir_cometido():
    c = str(input('\n \n ¿Qué tipo de palíndromo quiere verificar? (Elija una opción)\n '
                  '(1) - Numero natural, (2) - Frase): '))
    if c not in ['1', '2']:
        print('Cometido incorrecto, introduzca (1) o (2) para usar el cometido deseado')
        c = pedir_cometido()
    return c


def pedir_preguntado(cometido):
    preguntado = ''
    if cometido == '1':
        preguntado = str(input('Indique un número natural (ej. 12321): '))
        preguntado = f'C:{preguntado}'
    elif cometido == '2':
        preguntado = str(input('Indique una frase (ej. asa): '))
        preguntado = f'P:{preguntado}'

    return preguntado