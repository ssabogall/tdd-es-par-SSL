import unittest
from math_utils import es_multiplo_de

class TestEsMultiploDe(unittest.TestCase):
    def test_4_es_multiplo_de_2(self):
        self.assertTrue(es_multiplo_de(4, 2))

if __name__ == "__main__":
    unittest.main()