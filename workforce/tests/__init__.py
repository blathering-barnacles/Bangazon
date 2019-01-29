import unittest

def suite():
    return unittest.TestLoader().discover("workforce.tests", pattern="*.py")