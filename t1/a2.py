#a2.py

def myCheck(ipP, opP):
    print "myCheck: ", ipP, opP
    opP[0] = 2 * ipP
    #opP = 2 * ipP
    print "myCheck: ", ipP, opP
    return 0

def ONEtest_okay():
    """
    okay() should return ?
    """
    rsltMy=[0]
    print "ONEtest_okay: rsltMy[0]= ", rsltMy[0]
    print "ONEtest_okay: rsltMy= ", rsltMy
    rtrn = myCheck(234, rsltMy)
    ans1 = True
    print "ONEtest_okay ans1= ", ans1
    print "ONEtest_okay rtrn= ", rtrn
    print "ONEtest_okay: rsltMy[0]= ", rsltMy[0]
    print "ONEtest_okay: rsltMy= ", rsltMy

ONEtest_okay()
