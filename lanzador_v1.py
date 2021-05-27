import cliente_v1 as cli
# import servidor as serv
import servidor as serv

opcion = str(input("Introduzca (1) para ejecutar Servidor o (2) para Cliente: "))
if opcion == '1':
    print('Eligió ejecutar servidor')
    serv.servidor()
elif opcion == '2':
    cli.cliente()
else:
    print('Error en la introducción de datos')