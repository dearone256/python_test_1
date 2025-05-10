# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_name_group (app):
	app.session.Login(username="admin", password="secret")
	app.group.modify_first_group(Group(name1="New Name"))
	app.session.Logout()

def test_modify_name_header (app):
	app.session.Login(username="admin", password="secret")
	app.group.modify_first_group(Group(header1="New Header"))
	app.session.Logout()