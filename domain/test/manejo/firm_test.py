# -*- coding: utf-8 -*-
import unittest

from domain.manejo.firm.repository import FirmRepository
from domain.test import prepara_base_de_testes_domain


class FirmDomainTest(unittest.TestCase):
    def setUp(self):
        self.__session = prepara_base_de_testes_domain()
        self.repository = FirmRepository()

    def test_should_be_possible_to_getting_a_firm(self):
        result = self.repository.all(self.__session)
        self.assertEquals(1, len(result))


    def test_should_be_possible_to_create_a_new_firm(self):
        data = {'name':'Agrines 2'}
        new_firm = self.repository.new(**data)

        self.assertEqual(1, len(self.repository.all(self.__session)))
        result = self.repository.save(self.__session, new_firm)
        self.assertEqual(2, len(self.repository.all(self.__session)))
        self.assertEquals(result.name, 'Agrines 2')


    def test_should_be_possible_to_update_a_firm(self):

        result_edit = self.repository.first(self.__session)
        self.repository.update(self.__session, result_edit, **{'name': "SUPER AGRINES"})
        result = self.repository.first(self.__session)
        self.assertEqual(result.name, "SUPER AGRINES")


    def test_should_be_possible_to_delete_a_firm(self):
        firm_to_delete = self.repository.first(self.__session, **{'name': 'AGRINES'})
        self.assertEqual(1, len(self.repository.all(self.__session)))
        self.repository.delete(self.__session, firm_to_delete)
        self.assertEqual(0, len(self.repository.all(self.__session)))
