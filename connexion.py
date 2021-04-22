#!/usr/bin/python
# -*- coding= utf-8

from mod_python import Session
from mod_python import apache
fonctions = apache.import_module("fonctions")

def index(req):
    req.content_type = "text/html"
    conn = fonctions.connexionBD()
    cursor = conn.cursor()
    id_util = req.form["id_util"]
    login = req.form["login"]
    requete = "select id_util, mdp from util where login = %s"
    cursor.execute(requete, (login))
    tup = cursor.fetchone()
    if tup is None:
        msg = "Login inexistant"
        lien = fonctions.lien("form-connexion.py","Retour au formulaire de connexion")
    else:
        (id_util, mdp) = tup
        if mdp != req.form["mdp"]:
            msg = "Mot de passe incorrect"
            lien = fonctions.lien("form-connexion.py","Retour au formulaire de connexion")
        else:
            session = Session.Session(req)
            session["id_util"] = id_util
            session["login"] = login
            session.save()
            msg = "Le mot de passe est correct."
            lien = fonctions.lien("menu.py","Accès au menu du site")
    body = msg + "<br/>" + lien
    req.write(fonctions.codeHTML("Connexion", body))
