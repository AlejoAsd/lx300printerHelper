#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'torresmateo'
from escpos import *
from lx300printer.json_document import JsonDocument
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/print/", methods=['POST'])
def print_document():
    json_str = str(request.form['text'])
    response_str = "Your printer should be making some noise!!"
    try:
        epson = printer.Usb(0x04b8, 0x0046)
        epson.set(codepage='iso8859_9', font='c')
        if "verbatim" in request.form.keys():
            epson._raw(json_str)
        else:
            document = JsonDocument(json_str)
            epson._raw(document.get_printable_string())
    except Exception, e:
        response_str = "Error: " + str(e)
    finally:
        try:
            epson.close()
        except NameError:
            pass

    return response_str

@app.route("/", methods=['POST', 'GET'])
def hello():
    if "text" in request.form.keys():
        json_str = request.form["text"]
        document = JsonDocument(json_str)
        return render_template('preview.html', text=document.get_printable_string(), json_str=json.dumps(json_str))
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True, port=52738)