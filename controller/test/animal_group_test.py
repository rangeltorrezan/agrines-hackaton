# coding=utf-8

from controller.rest import create_app
from controller.test.test_utils import create_test_database_controller
from controller.test.test_utils import mock_publisher_uuid
from controller.test.test_utils import mock_elasticsearch_url

import unittest
import json


class BankControllerTest(unittest.TestCase):
    """
    Test the Bank Controller.
    """

    def setUp(self):
        mock_publisher_uuid(self)
        mock_elasticsearch_url(self)

        app = create_app('config')
        create_test_database_controller(app)
        self.app = app.test_client()
        self.app.testing = True
        self.headers = [('Content-Type', 'application/json')]

    def test_should_get_all_banks(self):
        # GIVEN
        response = self.app.get('/bank')

        # WHEN
        response_json = json.loads(response.data.decode('utf-8'))

        # THEN
        self.assertEqual(len(response_json), 1)

    def test_should_get_bank_by_code(self):
        # GIVEN
        response = self.app.get('/bank/237')

        # WHEN
        response_json = json.loads(response.data.decode('utf-8'))

        # THEN
        self.assertEqual(response_json['code'], '237')

    def test_should_create_bank(self):
        # GIVEN
        data = {'name': "BANCO DO BRASIL", 'code': "001"}

        # WHEN
        response = self.app.post('/bank', headers=self.headers, data=json.dumps(data))
        response_json = json.loads(response.data.decode('utf-8'))

        # THEN
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json['name'], 'BANCO DO BRASIL')

    def test_should_update_banking_agreement(self):
        # GIVEN
        data = {'code': '237', 'name': "NOVO BRADESCO"}

        # WHEN
        response = self.app.put('/bank/237', headers=self.headers, data=json.dumps(data))
        response_json = json.loads(response.data.decode('utf-8'))

        # THEN
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json['name'], 'NOVO BRADESCO')

    def test_should_delete_group(self):
        # GIVEN
        self.app.delete('/bank/237')

        # WHEN
        response = self.app.get('/bank')
        response_json = json.loads(response.data.decode('utf-8'))

        # THEN
        self.assertEqual(0, len(response_json))
