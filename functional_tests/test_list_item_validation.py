from .base import FunctionTest
from selenium.webdriver.common.keys import Keys
from unittest import skip

class ItemValidationTest(FunctionTest):
    
    def test_cannot_add_empty_list_items(self):

        self.fail('Write me!')
