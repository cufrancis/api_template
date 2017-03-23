#!/usr/bin/env python
# coding=utf-8

from api.handler.APIHandler import APIHandler

class index(APIHandler):
    def get(self):
        data = {
            'users':'/users/:username'
        }
        self.write_error(data, 404)
