# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group (app):
	app.session.Login(username="admin", password="secret")
	app.group.Create(Group(name1='05', header1='05', footer1='05'))
	app.session.Logout()

def test_add_empty_group (app):
	app.session.Login(username="admin", password="secret")
	app.group.Create(Group(name1='', header1='', footer1=''))
	app.session.Logout()