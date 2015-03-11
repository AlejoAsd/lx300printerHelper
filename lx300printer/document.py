#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'torresmateo'

from spanish_constants import *

class Document():

    def __init__(self):
        self.field_collection = {}
        self.document_width = 95
        self.main_string = u''

    '''detecta las colisiones entre los campos'''
    def check_collisions(self, candidate_field):
        for field in self.field_collection.values():
            #si el campo nuevo esta metido en el espacio ocupado por otro campo
            if field.y == candidate_field.y and \
               (field.x <= candidate_field.x <= field.x + field.length or
                 field.x <= candidate_field.x + candidate_field.length <= field.x + field.length):
                return False
        return True

    '''detecta si el campo es contenido dentro del documento'''
    def check_width(self, candidate_field):
        return candidate_field.x + candidate_field.length < self.document_width

    def add_field(self, field, ignore_collisions=False):
        if self.check_width(field):
            if ignore_collisions:
                self.field_collection[field.get_index(self.document_width)] = field
            else:
                if self.check_collisions(field):
                    self.field_collection[field.get_index(self.document_width)] = field
                else:
                    print "Error: el campo con texto: " + field.text + \
                          " colisiona con otro campo"
        else:
            print "Error: el campo con texto: " + field.text + " sobrepasa el ancho del documento"
        self.update_main_string()

    def update_main_string(self):
        current_index = 0
        self.main_string = unicode("")
        sorted_keys = sorted(self.field_collection.keys())
        for key in sorted_keys:
            #obtener el campo
            field = self.field_collection[key]
            #rellenar de espacios vacios el string
            for i in range(current_index, field.get_index(self.document_width)):
                if i % self.document_width == 0:
                    if i > 0:
                        self.main_string += unicode('\n')
                else:
                    self.main_string += unicode(' ')
                current_index += 1
            #agregar el texto del campo
            if current_index % self.document_width == 0:
                self.main_string += unicode('\n')
                current_index += 1
            self.main_string += field.text[:field.length]
            current_index += field.length
        self.main_string += unicode('\n')

    def get_printable_string(self):
        printable_string_bytes = self.main_string.encode('utf8')
        for character in spanish_characters:
            printable_string_bytes = printable_string_bytes.replace(character, spanish_characters[character])

        return printable_string_bytes