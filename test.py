#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mod_python
import fonctionsCor

def index(req):
	titre = "Hello world"
	corps = "Bonjour"
	req.content_type = "text/html"
	req.write(fonctionsCor.codeHTML(titre, corps))