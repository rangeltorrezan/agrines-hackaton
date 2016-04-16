# -*- coding: utf-8 -*-
import unittest

from domain.manejo.animal_group.repository import AnimalGroupRepository
from domain.test import prepara_base_de_testes_domain


class FarmDomainTest(unittest.TestCase):
    def setUp(self):
        self.__session = prepara_base_de_testes_domain()
        self.repository = AnimalGroupRepository()

    def test_should_be_possible_to_getting_an_animal_group(self):
        result = self.repository.all(self.__session)
        self.assertEquals(1, len(result))


    def test_should_be_possible_to_create_an_animal_group(self):
        data = {'name':'Grupo de Elite', 'farm_id': 1}
        new_firm = self.repository.new(**data)

        self.assertEqual(1, len(self.repository.all(self.__session)))
        result = self.repository.save(self.__session, new_firm)
        self.assertEqual(2, len(self.repository.all(self.__session)))
        self.assertEquals(result.name, 'Grupo de Elite')
        self.assertEquals(result.situation, 'O')


    def test_should_be_possible_to_update_an_animal_group(self):

        result_edit = self.repository.first(self.__session)
        self.repository.update(self.__session, result_edit, **{'name': "PigElite"})
        result = self.repository.first(self.__session)
        self.assertEqual(result.name, "PigElite")


    def test_should_be_possible_to_delete_an_animal_group(self):
        firm_to_delete = self.repository.first(self.__session, **{'name': 'LOTE DE PORQUINHOS'})
        self.assertEqual(1, len(self.repository.all(self.__session)))
        self.repository.delete(self.__session, firm_to_delete)
        self.assertEqual(0, len(self.repository.all(self.__session)))
