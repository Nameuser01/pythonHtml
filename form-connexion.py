#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mod_python
import fonctions
from mod_python import util

def index(req):
	req.content_type = "text/html"
	titre = "exo5"
	corps = "<form action=\"test.html\" method=\"post\"><input name=\"login\" type=\"text\" maxlength=\"20\" placeholder=\"Login\" /><input name=\"pwd\" type=\"password\" maxlength=\"20\" placeholder=\"Password\" /><input type=\"submit\"</form><a href=\"menu.py\">Redirection manuelle</a>"
	req.write(fonctions.codeHTML(titre, corps))