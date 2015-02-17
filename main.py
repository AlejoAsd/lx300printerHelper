#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'torresmateo'
from lx300printer.json_document import JsonDocument
from flask import Flask, render_template, request, redirect, url_for
import json
import usb.core
import os

app = Flask(__name__)

@app.route("/print/", methods=['POST'])
def print_document():
    json_str = str(request.form['text'])
    response_str = "Your printer should be making some noise!!"
    hola = open("hola.txt", "w")
    try:
        if "verbatim" in request.form.keys():
            hola.write(json_str)
        else:
            document = JsonDocument(json_str)
            hola.write(document.get_printable_string())
        hola.close()
        os.system('RawPrinterConsole')
        print "asdasdasd"
    except Exception, e:
        response_str = "Error: " + str(e)

    return response_str

@app.route("/", methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        json_str = request.form["text"]
        if "verbatim" in request.form.keys():
            return redirect(url_for('print_document'), code=307)
        else:
            document = JsonDocument(json_str)
            return render_template('preview.html', text=document.get_printable_string(), json_str=json.dumps(json_str))
    else:
        return render_template('index.html')


@app.route("/config", methods=['POST', 'GET'])
def config():
    if request.method == 'POST':
        return "Not yet implemented!!"
    else:
        all_devices = usb.core.find(find_all=True)
        dev = {}
        for device in all_devices:
            dev[(hex(device.idVendor), hex(device.idProduct))] = device.product
        return render_template('config.html', dev=dev)

if __name__ == "__main__":
    app.run(debug=True, port=52738)