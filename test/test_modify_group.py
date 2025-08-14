# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_name_group (app):
	if app.group.count() == 0:
		app.group.Create(Group(name1="precondition_group"))
	app.group.modify_first_group(Group(name1="New Name"))

def test_modify_name_header (app):
	if app.group.count() == 0:
		app.group.Create(Group(header1="precondition_group"))
	app.group.modify_first_group(Group(header1="New Header"))