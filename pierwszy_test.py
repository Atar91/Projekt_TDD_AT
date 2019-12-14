import unittest
import moj_program

class Test1TDD(unittest.TestCase):

    def test_100(self):
        wyniki = moj_program.zwroc_100()
        self.assertEqual(100, wyniki)

    def test_zwroc_parametr(self):
        ret = moj_program.zwroc_parametr('Olek')
        self.assertEqual('Olek', ret)

if __name__ == '__main__':
    unittest.main()
