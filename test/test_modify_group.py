# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_name_group (app):
	app.group.modify_first_group(Group(name1="New Name"))

def test_modify_name_header (app):
	app.group.modify_first_group(Group(header1="New Header"))