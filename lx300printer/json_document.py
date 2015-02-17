#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'torresmateo'

from document import Document
from field import  Field
import json


class JsonDocument(Document):
    json_object = None

    def __init__(self, json_str):
        self.json_object = json.loads(json_str)
        for field in self.json_object["fields"]:
            self.add_field(Field(str(field["text"]), field["x"], field["y"], field["length"]))
        if "document_width" in self.json_object:
            self.document_width = self.json_object["document_width"]


if __name__ == "__main__":
    json_str_x = '''
{
    "document_width":95,
    "fields": [
        {
            "text": "hola",
            "x": 1,
            "y": 0,
            "length": 4
        },
        {
            "text": "chau",
            "x": 1,
            "y": 2,
            "length": 4
        },
        {
            "text": "asdfkjan",
            "x": 1,
            "y": 2,
            "length": null
        }
    ]
}
'''
    json_doc = JsonDocument(json_str_x)
    print json_doc.get_printable_string()