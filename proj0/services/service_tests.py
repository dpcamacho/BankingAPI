import unittest

from models.client import Client
from services.client_services import ClientServices as cs
from services.account_services import AccountServices as acc


class TestServices(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_client(self):
        assert cs.get_client_by_id(1)

    def test_get_all_clients(self):
        assert cs.all_clients()

    def test_get_all_accounts(self):
        assert acc.all_accounts("1")


if __name__ == '__main__':
    unittest.main()
