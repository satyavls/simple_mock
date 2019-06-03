import unittest
from add_module import add_num
from simple_mock import SimpleMock


class TestAddNum(unittest.TestCase):

    def setUp(self):
        self.simple_mock = SimpleMock()

    def test_add_num(self):
        patched_add_func = self.simple_mock.patch_func(func='add_num', exptd_ret_val=45)
        self.assertEqual(add_num(2, 2), 45)


if __name__ == '__main__':
    unittest.main()
