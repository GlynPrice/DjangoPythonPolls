#classRepr.py

class foo():
  fixed = "Foo: Welcome"
  def setData(self, inData):
    self.dataOne = inData
  setData.shortDescription = "Hello"
  def __repr__(self):
    return "rrrrrrr"
  def __unicode__(self):
    return "uuuuuuuu"

print foo
print str(foo)
i1 =foo()
print i1
print i1.__repr__()
print i1.__unicode__()

i1.setData(1833)
print i1.dataOne
print i1.setData.shortDescription



