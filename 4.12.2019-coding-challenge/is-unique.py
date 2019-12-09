import unittest


def is_unique(string):
    # if string == '': return True

    chr_list=[None]*256
    for c in string:
        if chr_list[ord(c)] is not None:
            return False
        chr_list[ord(c)] = c
    return True

print(is_unique(''))

class MyTestCase(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), (''), ('house')]
    dataF = [('23ds2'), ('hb 627jh=j ()'), ('hello')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)

if __name__ == '__main__':
    unittest.main()

