# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def  app(request):
	fixture = Application()
	request.addfinalizer(fixture.destroy)
	return fixture

def test_add_group (app):
	app.session.Login(username="admin", password="secret")
	app.Create_group( Group(name1='05', header1='05', footer1='05'))
	app.session.Logout()

def test_add_empty_group (app):
	app.session.Login(username="admin", password="secret")
	app.Create_group(Group(name1='', header1='', footer1=''))
	app.session.Logout()