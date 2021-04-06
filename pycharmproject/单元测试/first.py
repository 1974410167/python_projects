

import unittest

a = 1
b = 'hello world ss'

class TestDict(unittest.TestCase):
    def setUp(self) -> None:
        print('start')

    def tearDown(self) -> None:
        print('end')

    def test_init(self):
        self.assertEqual(a,1)

    def test_str(self):
        with self.assertRaises(TypeError):
            b.split(2)


if __name__=='__main__':
    a = TestDict()
    print(a)
    














