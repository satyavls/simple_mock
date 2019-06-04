####
# simple_mock
####
    
************
## Introduction
************

The motivation behind this library is to provide easy way of mocking to python functions while doing the unittest.\
This library is based on "mock" module in python  
 
 
************
## Installation
************

Install via [pip](http://www.pip-installer.org/):

    $ pip install simple_mock

Install from source:

    $ git clone https://github.com/satyavls/simple_mock.git
    $ cd simple_mock
    $ python setup.py install

## Usage

```python
# example - mocking single function to return some value or exception

import unittest
from simple_mock import SimpleMock

# import of function that needs to be patch in test case file
from add_module import add_num


class TestAddNum(unittest.TestCase):

    def setUp(self):
        # create simple mock object 
        self.simple_mock = SimpleMock()

    def tearDown(self):
        self.simple_mock.clear_all_patch()

    def test_add_num(self):
        """
        This is example where add_num function is patched to return the 45 value
        """
        # patch the add_num function to return 45 value
        patched_add_func = self.simple_mock.patch_func(func='add_num', exptd_ret_val=45)
        self.assertEqual(add_num(2, 2), 45)

    def test_add_num_exception(self):
        """
        This is exmaple where add_num function is patched to return exception
        """
        # Patch the add_num function to return ValueError 
        patched_add_func = self.simple_mock.patch_func(func='add_num', exptd_err=ValueError,
                                                       err_msg="exception raise in add_num")
        self.assertRaises(ValueError, add_num)


if __name__ == '__main__':
    unittest.main()

```
Refer [here](https://github.com/satyavls/simple_mock/tree/master/examples) for more detailed examples 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests or examples are appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
