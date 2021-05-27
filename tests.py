import unittest

import servidor_v2_select as servidor


class tests(unittest.TestCase):
    def test_01_frase(self):
        # servidor
        pedido = 'P:asa'
        resultado = servidor.generar_respuesta(pedido)
        self.assertEqual('SI', resultado)
    def test_02_frase(self):
        # servidor
        pedido = 'P:A man, a plan, a canal: Panama'
        resultado = servidor.generar_respuesta(pedido)
        self.assertEqual('PARCIAL', resultado)
    def test_03_frase(self):
        # servidor
        pedido = 'P:Qué tontería'
        resultado = servidor.generar_respuesta(pedido)
        self.assertEqual('NO', resultado)
    def test_04_numero(self):
        # servidor
        pedido = 'C:13431'
        resultado = servidor.generar_respuesta(pedido)
        self.assertEqual('SI', resultado)
    def test_05_numero(self):
        # servidor
        pedido = 'C:428'
        resultado = servidor.generar_respuesta(pedido)
        self.assertEqual('NO', resultado)
    def test_06_numero(self):
        # servidor
        pedido = 'C:Qué tontería'
        resultado = servidor.generar_respuesta(pedido)
        self.assertEqual('NONATURAL', resultado)
    def test_07(self):
        # servidor
        pedido = 'Cualquier otro mensaje'
        resultado = servidor.generar_respuesta(pedido)
        self.assertEqual('ERROR', resultado)
