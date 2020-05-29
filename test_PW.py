import unittest
from PasswordGenerator import keyWord

class MyTest(unittest.TestCase):
    def test_keyWord(self):
        keyWordList = ["Yes", "No"]
        pw = "pq39ade8h83sh"
        pw = keyWord(keyWordList, pw)
        if pw.index(keyWordList[0]) == True and pw.index(keyWordList[1]):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()