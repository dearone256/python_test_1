# -*- coding: utf-8 -*-
import pytest
from model.contact_fields import ContactFields


def test_add_contact (app):
	app.contact.Create_contact(ContactFields(firstname='FRname', middlename='MDname', lastname='LTname',
                                             nickname='NKname', title='Title1', company='Company1', address='Address1',
                                             home='Home1', mobile='999', work='888', fax='777',
                                             email2='second_mail@company.test', homepage='homepage.test', birth_day='3',
                                             birth_month='August', birth_year='1981', address2='secondary_address',
                                             phone2='secondary_home_phone', notes='secondary_notes'))

def test_add_empty_contact_with_group (app):
	app.contact.Create_contact(ContactFields(firstname='', middlename='', lastname='',
                                             nickname='', title='', company='', address='',
                                             home='', mobile='', work='', fax='',
                                             email2='', homepage='', birth_day='',
                                             birth_month='', birth_year='', address2='',
                                             phone2='', notes=''))