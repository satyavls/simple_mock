####
# simple_mock
####
    
************
## Introduction
************

The motivation behind this library is to provide easy way of mocking to python functions while doing the unittest.
This library use the mock module in python  
 
 
************
##Installation
************

Install via `pip`_:

    $ pip install simple_mock

Install from source:

    $ git clone https://github.com/satyavls/simple_mock.git
    $ cd simple_mock
    $ python setup.py install

## Usage

```python
# example of simple mock - single function 

import unittest
from simple_mock import SimpleMock

# import of function that needs to be patch in test case file
from add_module import add_num

class TestAddFunctionality(unittest.TestCase):
    def setUp(self):
        self.mock_obj = SimpleMock()
    
    def test_add_return_val(self):
        # add_num function patched to return 45 value 
        patched_add_func = self.mock_obj.patch_func(func='add_num',exptd_ret_val=45)
        self.assertEqual(add_num(2,2),45)

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests or examples are appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)