#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'torresmateo'
from escpos import *
from lx300printer.document import Document
from lx300printer.field import Field
from flask import Flask
from flask import render_template

app = Flask(__name__)
import json

documento = Document()
documento.document_width = 95
documento.add_field(Field("prueba", 0, 0))
documento.add_field(Field("prueba", 0, 1))
documento.add_field(Field("prueba", 0, 2))
documento.add_field(Field("prueba", 0, 3))
#documento.add_field(Field("pruebaasd", 0, 4))
documento.add_field(Field("-" * 94, 0, 4))
# documento.add_field(Field("prueba", 5, 1))
# documento.add_field(Field("prueba", 7, 2))
# documento.add_field(Field("prueba", 87, 3))
# documento.add_field(Field("-" * 94, 0, 7))

@app.route("/print/", methods=['POST'])
def magic_please():
    personId = int(request.form['personId'])
    epson = printer.Usb(0x04b8, 0x0046)
    epson.set(codepage='iso8859_9', font='c')

    epson._raw(documento.get_printable_string())

    epson.close()

    return "Imprimiste!!"

@app.route("/")
def hello():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)