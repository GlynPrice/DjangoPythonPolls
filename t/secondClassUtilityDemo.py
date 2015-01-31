#firstClassDemo.py

class zBase:
  zFixed = "Welcome to the z World"

  #Representation of this object: zBase
  # __unicode__ on Python 2, __str__ for Python 3
  def __unicode__(self):
    return str(zBase) + "  " + self.zFixed
  def __str__(self):
    return str(zBase) + "  " + self.zFixed

  def __init__(self, NameBase):
    self.zName= NameBase
    self.zData1 = 0
    self.zData2 = 0
  def setZdata1(self, z1):
    self.zData1 = z1
  def setZdata2(self, z2):
    self.zData2 = z2
  def mod_zFixed(self, ipSg):
    zBase.zFixed = zBase.zFixed + ipSg

class analyseData(zBase):
  dataFixed = 42
  def __init__(self, who):
    self.name = who
    self.data1 = 0
    self.data2 = 0
    self.data3 = 0
  def setdataFirst(self, dataFirst):
    self.data1 = dataFirst
  def setdataSecond(self, dataSecond):
    self.data2 = dataSecond
  def utilOne(self, ipDataP):
    print "utilOne: ipDataP= ", ipDataP
    print self.data1, self.data2, self.data3
    print "okay"
    print "dataFixed= ", self.dataFixed, "zFixed= ", self.zFixed

print zBase
aZbase = zBase("Hello")
print aZbase.__unicode__()
print aZbase.__str__()

print analyseData
qMe = analyseData("Glyn")
print qMe
print qMe.zFixed
qMe.dataFixed=1833
qMe.setdataFirst(3.14159)
qMe.setdataSecond(2.71828)
print qMe.name, qMe.dataFixed, qMe.data1, qMe.data2, qMe.data3

print zBase.zFixed + ", " + qMe.name

print zBase.zFixed
qMe.mod_zFixed(":-  ")
print zBase.zFixed
print zBase.zFixed + qMe.name

myZbase = zBase("okay")
print myZbase.zName, myZbase.zData1, myZbase.zData2

rtrnU = qMe.utilOne(123321)


