import unittest

from loadbalancer1 import fetchLinkCost

class Testloadbalancer(unittest.TestCase):
    def test_fetchlinkcost(self,portKey):
        try:
            self.assertEqual(type(portKey)==int)
        except ValueError as e:
            ValueError



