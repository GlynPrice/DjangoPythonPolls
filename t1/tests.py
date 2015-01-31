#tests.py
print "\nHello, this is t1/tests.py\n"

from django.test import TestCase

class QuestionMethodTests(TestCase):

  def test_XyZ(self):
    """
    XyZ() should return True
    """
    print "test_XyZ"
