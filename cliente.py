import socket
import sys
from time import sleep


def pedir_direccion():
    print('¿Indique la dirección y puerto del servidor?')
    host = str(input('Dirección (tip: localhost): '))
    port = int(input('Puerto (tip: 16033): '))
    return host, port


def cliente():
    st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # host = 'localhost'
    # port = 16033
    host, port = pedir_direccion()
    try:
        st.connect((host, port))
    except socket.gaierror:
        print("Error: la dirección o el puerto del servidor son incorrectos")
        sys.exit()

    repeticiones = 3
    while repeticiones != 0:
        cometido = pedir_cometido()
        preguntado = pedir_preguntado(cometido)
        st.send(bytes(preguntado, "utf-8"))
        respuesta = st.recv(128)
        print(f'Respuesta: {respuesta.decode("utf-8")}')

        repeticiones -= 1

    st.close()


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
