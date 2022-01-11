import unittest
from poetry_sub.my_fun import MyFun

class TestMain(unittest.TestCase):
    MyFun()


if __name__ == '__main__':
    unittest.main()