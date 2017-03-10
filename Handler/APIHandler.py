#!/usr/bin/env python
# coding=utf-8

import json
from tornado.web import Finish
import tornado.web

class APIHandler(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.set_header('Content-Type', 'text/json')
        self.set_header('Server', 'Tornado')
        self.set_header('Connection','keep-alive')

        if self.settings.get('allow_remote_access'):
            self.access_control_allow()

    def write_json(self, data, status_code=200, msg='success.'):
        self.set_header('Cache-Control', "no-cache")
        self.set_status(status_code)

        self.write(json.dumps({
            'meta':status_code,
            'data':data,
            'msg':msg,
        }))
        raise Finish()
