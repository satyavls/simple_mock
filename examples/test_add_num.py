import unittest
from add_module import add_num
from simple_mock import SimpleMock


class TestAddNum(unittest.TestCase):

    def setUp(self):
        self.simple_mock = SimpleMock()

    def test_add_num(self):
        """
        This is example where add_num function is patched to return the 45 value
        """
        patched_add_func = self.simple_mock.patch_func(func='add_num', exptd_ret_val=45)
        self.assertEqual(add_num(2, 2), 45)

    def test_add_num_exception(self):
        """
        This is exmaple where add_num function is patched to return exception
        """

        patched_add_func = self.simple_mock.patch_func(func='add_num', exptd_err=ValueError,
                                                       err_msg="exception raise in add_num")
        self.assertRaises(ValueError, add_num)


if __name__ == '__main__':
    unittest.main()
