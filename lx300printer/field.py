#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'torresmateo'

from spanish_constants import *

class Field():
    x = 0
    y = 0
    length = 0
    text = ""

    def __init__(self, text, x, y, length=None):
        #si no se establecio la longitud se toma la lingitud del texto
        self.x = x
        self.y = y
        self.text = text
        #reemplazar los caracteres del campo
        for character in spanish_characters.keys():
            self.text = self.text.replace(character, spanish_characters[character])
        if length is None:
            self.length = len(text)
        else:
            self.length = length

    def get_index(self, document_width):
        return document_width * self.y + self.x