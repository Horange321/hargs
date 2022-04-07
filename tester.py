import unittest

from hargutil import Hargs


class Tester1(unittest.TestCase):
    def test1(self):
        a = Hargs(['-v', '-a=asd', '--force=true'])
        a.add('v', 'version', 'v') \
            .add('a', '', 'asd') \
            .add('', 'force', 'f') \
            .add('', 'none', 'none')
        ar = a.to_dict()

        self.assertEqual(None, ar['v'])
        self.assertEqual("asd", ar['asd'])
        self.assertEqual("true", ar['f'])
        self.assertEqual(None, ar['none'])


if __name__ == '__main__':
    unittest.main()
