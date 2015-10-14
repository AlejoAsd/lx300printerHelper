#-*- coding: utf-8 -*-
from escpos import *

# Abrir la impresora
ep = printer.Usb(0x4b8, 0x202)

def imprimir(texto):
	ep.text(texto + '\n' * 3)
	ep.cut()

# Crear la grilla
separadores = ('.' * 9)
numeros = map(str, list(range(0, 10)))

imprimir(separadores.join(numeros))
