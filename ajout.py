#!/usr/bin/python

import fonctions

fonctions.connexionBD()

conn = .cursor()
conn.execute("INSERT INTO contact(nom, email, tel, adresse) VALUES(?, ?, ?, ?,)",(nom, email, tel, adresse))
