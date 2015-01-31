#myStuff321.py
print "Hello, this is polls/t/myStuff321.py"

from django.test import TestCase

class ABC(TestCase):

  #def __init__(self):
  #  print "ABC"
  def setUp(self):
    print "class:  ABC",

  def test_AbcBook(self):
    """
    Abc() should return True
    """
    print "def:  test_AbcBook"

  def testMessage(self):
    """
    Abc() should return True
    """
    print "def: testMessage "

class Kwik(TestCase):
  def setUp(self):
    print "class:  Kwik",

  def test_Number1(self):
    """
    Abc() should return True
    """
    print "def: test_Number1"

  def test_Number2(self):
    """
    Abc() should return True
    """
    print "def: test_Number2"

  def util1066okay(self):
    """
    Abc() should return True
    """
    print "def: util1066okay"


