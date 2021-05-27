import socket
import time
from _socket import SHUT_RDWR
import string

def servidor():
    st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Servidor levantado')
    host = 'localhost'
    port = 16033
    st.bind((host,port))
    st.listen(3)

    while True:
        nuevo_socket, nueva_ruta_socket = st.accept()
        escucha = (nuevo_socket.recv(128)).decode('utf-8')
        respuesta = generar_respuesta(escucha)
        nuevo_socket.send(bytes(respuesta, "utf-8"))
        nuevo_socket.close()


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

