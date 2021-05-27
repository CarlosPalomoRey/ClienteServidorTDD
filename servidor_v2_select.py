import select
import socket
import sys
import time
from _socket import SHUT_RDWR
import string


def print_to_stderr(*a):
    # Here a is the array holding the objects
    # passed as the argument of the function
    print(*a, file=sys.stderr)


def servidor():
    st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    st.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Servidor levantado')
    host = 'localhost'
    port = 16033
    st.bind((host, port))
    st.listen()

    lista_sockets = [st]
    while True:
        lista_ready, _, _ = select.select(lista_sockets, [], [])
        for fd in lista_ready:
            if fd == st:
                # import pdb; pdb.set_trace()
                cliente, ruta_cliente = st.accept()
                imprimir = 'Dirección cliente: ' + str(ruta_cliente[0]) + ' ' + str(ruta_cliente[1])
                print_to_stderr(imprimir)
                lista_sockets.append(cliente)
            else:
                peticion = fd.recv(1024)
                if not peticion:
                    # cierre de cliente
                    lista_sockets.remove(fd)
                    fd.close()
                else:
                    # hay petición: se gestiona
                    imprimir = 'Petición cliente: ' + peticion.decode('utf-8')
                    print_to_stderr(imprimir)
                    respuesta = generar_respuesta(peticion.decode('utf-8'))
                    fd.send(bytes(respuesta, "utf-8"))


def generar_respuesta(escucha):
    resultado = 'ERROR'
    if escucha.startswith('C:'):
        numero = escucha[2:]
        if numero == numero[::-1]:
            resultado = 'SI'
        else:
            resultado = 'NO'
        for e in numero:
            if e not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                resultado = 'NONATURAL'
    if escucha.startswith('P:'):
        frase = (escucha[2:]).lower()
        frase_procesada = ''.join(f for f in frase if f.isalnum())
        if frase == frase[::-1]:
            resultado = 'SI'
        elif frase_procesada == frase_procesada[::-1]:
            resultado = 'PARCIAL'
        else:
            resultado = 'NO'

    return resultado

