import unittest
from Employee import Employee_work


class TestEmployee_work(unittest.TestCase):
    def setUp(self):
        self.his_value=Employee_work('zhang','chao',10000); self.raises=['',2000]

    def test_give_default_raise(self):
        self.assertEqual(self.his_value.give_raise(self.raises[0]),15000)

    def test_give_custom_raise(self):
        self.assertEqual(self.his_value.give_raise(self.raises[1]),12000)


if __name__ == '__main__':
    unittest.main()