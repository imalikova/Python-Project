# -*- coding: utf-8 -*-

def test_login(app):
   # app.open_homepage()
   app.session.login("imalikova", "Estoyfeliz1234*")
   app.session.logout()
