#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import mod_python
from mod_python import util

def codeHTML(titre, corps):
	return """<!DOCTYPE html>
	<html lang="fr">
	<head>
	<title>""" + titre + """</title>
	<meta charset="utf-8">
	</head>
	<body>""" + corps + """</body>
	</html>"""

def lien(url, texte):
    return "<a href=\"" + url + "\">" + texte + "</a>"

def connexionBD():
    conn = psycopg2.connect("""host=localhost dbname=devweb password=123456 user=devweb""")
    return conn

def redirectionSiNonConnecte(req, s):
    if s.is_new():
        util.redirect(req, "form-connexion.py")