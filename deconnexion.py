#!/usr/bin/python
# -*- coding: utf-8 -*-

from mod_python import Session
from mod_python import util

def index(req):
    s = Session.Session(req)
    s.delete()
    util.redirect(req, "form-connexion.py")
