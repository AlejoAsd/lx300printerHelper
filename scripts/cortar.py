from escpos import *

epson = printer.Usb(0x4b8, 0x202)
epson.cut()
epson.close()