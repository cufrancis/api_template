#!/usr/bin/env python
# coding=utf-8

from .APIHandler import APIHandler

class index(APIHandler):
    def get(self):
        self.write_json({'name':'lxj'})
        # self.write("Index")
