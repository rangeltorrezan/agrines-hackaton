# -*- coding: utf-8 -*-
import unittest

from domain.manejo.farm.repository import FarmRepository
from domain.test import prepara_base_de_testes_domain


class FarmDomainTest(unittest.TestCase):
    def setUp(self):
        self.__session = prepara_base_de_testes_domain()
        self.repository = FarmRepository()

    def test_should_be_possible_to_getting_a_farm(self):
        result = self.repository.all(self.__session)
        self.assertEquals(1, len(result))


    def test_should_be_possible_to_create_a_new_farm(self):
        data = {'name':'Granja Chico Cunha', 'firm_id': 1, 'note':'Granja mais que dahora'}
        new_firm = self.repository.new(**data)

        self.assertEqual(1, len(self.repository.all(self.__session)))
        result = self.repository.save(self.__session, new_firm)
        self.assertEqual(2, len(self.repository.all(self.__session)))
        self.assertEquals(result.name, 'Granja Chico Cunha')


    def test_should_be_possible_to_update_a_farm(self):

        result_edit = self.repository.first(self.__session)
        self.repository.update(self.__session, result_edit, **{'name': "Granja Zika"})
        result = self.repository.first(self.__session)
        self.assertEqual(result.name, "Granja Zika")


    def test_should_be_possible_to_delete_a_farm(self):
        firm_to_delete = self.repository.first(self.__session, **{'name': 'GRANJA DA HORA'})
        self.assertEqual(1, len(self.repository.all(self.__session)))
        self.repository.delete(self.__session, firm_to_delete)
        self.assertEqual(0, len(self.repository.all(self.__session)))
