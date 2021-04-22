#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from mod_python import apache
from mod_python import Session
from mod_python import util
import fonctions

def index(req):
    session = Session.Session(req)
#    fonctions.redirectionSiNonConnecte(req, session)
    req.content_type = "text/html"
    body = """<h1>Menu principal</h1>
<br/>Vous êtes connecté en tant que <b>"""  """</b>.
<ul>
    <li><a href="form-ajout.py">Ajouter un contact</a></li>
    <li><a href="liste.py">Liste des contacts</a></li>
    <li><a href="deconnexion.py">Déconexion</a></li>
</ul>"""
    req.write(fonctions.codeHTML("Menu principal", body))
