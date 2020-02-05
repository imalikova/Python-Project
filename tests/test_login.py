# -*- coding: utf-8 -*-

def test_login(app):
   app.test_open_homepage()
   app.session.test_login(username="imalikova", password="Estoyfeliz1234*")
   app.session.test_logout()
