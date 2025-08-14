# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group (app):
	app.group.Create(Group(name1='05', header1='05', footer1='05'))

def test_add_empty_group (app):
	app.group.Create(Group(name1='', header1='', footer1=''))