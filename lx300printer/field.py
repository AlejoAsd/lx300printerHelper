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
        print type(self.text)
        #reemplazar los caracteres del campo
        for character in spanish_characters.keys():
            print character
            print type(character)
            print spanish_characters[character]
            print type(spanish_characters[character])
            
            #self.text = self.text.decode("utf-8")
            #self.text = self.text.replace(unicode(character), spanish_characters[character])
            self.text = self.text.replace(character, spanish_characters[character])
            print self.text
            #self.text = self.text.encode("utf-8")
        if length is None:
            self.length = len(text)
        else:
            self.length = length

    def get_index(self, document_width):
        return document_width * self.y + self.x
		
if __name__ == "__main__":
	test_field = Field(u"hñla", 0, 0)
	#u"hñla".decode("utf-8").replace("ñ", spanish_characters["ñ"]).encode("utf-8")
	'''
	print spanish_characters["ñ"]
	print repr(u"hñla")
	print u"hñla".encode("utf-8").replace("ñ", spanish_characters["ñ"])
	'''
	#.encode('utf8')
	
	
	
	