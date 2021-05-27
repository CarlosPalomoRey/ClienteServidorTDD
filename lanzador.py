import cliente as cli
# import servidor as serv
import servidor_v2_select as serv

opcion = str(input("Introduzca (1) para ejecutar Servidor o (2) para Cliente: "))
if opcion == '1':
    print('Eligió ejecutar servidor')
    serv.servidor()
elif opcion == '2':
    cli.cliente()
else:
    print('Error en la introducción de datos')