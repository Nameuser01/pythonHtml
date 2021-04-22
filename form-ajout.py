#!/usr/bin/python
# -*- coding:utf-8 -*-

import fonctions

def index(req):
	req.content_type = "text/html"
	titre = "exo10"
	body = """ <h4>Ajout d'un contact</h4>
	<form action="ajout.py" method="post"> 
	<label for="nom">Nom</label>
	<input name="nom" type="text" maxlenght="100" /><br />
	<label for="adresse">Adresse</label>
	<input name="adresse" type="text" maxlenght="100" /><br />
	<label for="email">Email</label>
	<input name="email" type"text" maxlenght="100" /><br />
	<label for="tel">Téléphone</label>
	<input name="tel" type="text" maxlenght="10" />
	<input type="submit" value="valider" /><br />
	<a href="menu.py">Retour au menu principal</a>
	"""
	req.write(fonctions.codeHTML(titre, body))
