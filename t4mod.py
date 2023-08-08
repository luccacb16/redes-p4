#!/usr/bin/env python3
import random
from slip import CamadaEnlace

class LinhaSerial:
    def __init__(self):
        self.callback = None
        self.fila = b''
    def registrar_recebedor(self, callback):
        self.callback = callback
    def enviar(self, dados):
        self.fila += dados

def rand_ip():
    return '%d.%d.%d.%d'%tuple(random.randint(1, 255) for i in range(4))

next_hop = rand_ip()
linha_serial = LinhaSerial()
enlace = CamadaEnlace({next_hop: linha_serial})
datagramas = []
def recebedor(datagrama):
    datagramas.append(datagrama)
enlace.registrar_recebedor(recebedor)

def caso(entrada, saida):
    for datum in entrada:
        linha_serial.callback(datum)
    assert datagramas == saida, 'Ao receber os dados %r pela linha serial, deveriam ter sido reconhecidos os datagramas %r, mas foram reconhecidos %r' % (entrada,saida,datagramas)
    datagramas.clear()

# Casos de teste com um único quadro
caso([b'CD\xdb\xdd\xc0'], [b'CD\xdb'])
