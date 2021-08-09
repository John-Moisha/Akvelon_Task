import unittest

'''Task for Akvelon, Pyaskovskiy Kiryll
The sequence of brackets is balanced'''

'''This class have method(check_balance) for check balanced of brackets'''
class BalanceVerificator:
    def __init__(self):
        self._stack = []
        self._index = 0
        self._brackets_dict = {")": "(", "]": "[", "}": "{"}

    '''Hide method, who return index not closed bracket'''
    def _not_balanced_answer(self):
        print(f"NOT BALANCED ({self._index}), returns {self._index}")
        return self._index

    '''Method, who check    1. check input value not empty, and return Error
                            2. check witch bracket broke the value, return index broken bracket 
                            3. check input line contains non-brackets values, return Error'''
    def check_balance(self, val):
        if not val:
            raise ValueError("Can't be empty")
        self._stack = []
        for self._index, symbol in enumerate(val):
            if symbol in self._brackets_dict.values():
                self._stack.append(symbol)
            elif symbol in self._brackets_dict:
                if len(self._stack) == 0:
                    return self._not_balanced_answer()
                elif self._stack[-1] == self._brackets_dict[symbol]:
                    self._stack.pop()
                elif self._stack[-1] != self._brackets_dict[symbol]:
                    return self._not_balanced_answer()
            else:
                raise ValueError(f"""A character "{symbol}" doesn’t belong to any known brackets type.""")
        if self._stack:
            return self._not_balanced_answer()
        else:
            print("BALANCED, returns -1")
            return -1


class MyTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._validator = BalanceVerificator()

    def test_1(self):
        value = self._validator.check_balance("{}")
        self.assertEqual(value, -1)

    def test_2(self):
        value = self._validator.check_balance("{[}")
        self.assertEqual(value, 2)

    def test_3(self):
        value = self._validator.check_balance("{([])}")
        self.assertEqual(value, -1)

    def test_4(self):
        value = self._validator.check_balance("{[(])]}")
        self.assertEqual(value, 3)

    def test_5(self):
        with self.assertRaises(Exception) as context:
            self._validator.check_balance("")
            self.assertTrue("Can't be empty" in context.exception)

    def test_6(self):
        with self.assertRaises(Exception) as context:
            self._validator.check_balance("s[]")
            self.assertTrue("A character s doesn’t belong to any known brackets type." in context.exception)


if __name__ == '__main__':
    unittest.main()
