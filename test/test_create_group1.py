# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application1 import Application1

@pytest.fixture
def apps(request):
	fixture = Application1()
	request.addfinalizer(fixture.destroy)
	return fixture

def test_create_group1(apps):
  apps.login(username="admin" , password="secret")
  apps.create_group(Group(name1="grname_04", header1="grheader_04", footer1="grfooter_04"))
  apps.logout()

def test_create_empty_group1(apps):
  apps.login(username="admin" , password="secret")
  apps.create_group(Group(name1="", header1="", footer1=""))
  apps.logout()











  
