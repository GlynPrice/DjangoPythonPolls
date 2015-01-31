#tB01viewResponse.py

#For this django-test method no temporary database is created;
#it is the existing database that is used. So db.sqlite3 must exist, but
#it can have any number of Questions: zero, one or more .

from django.test.utils import setup_test_environment
from django.test import Client

from django.core.urlresolvers import reverse

from polls.models import Question

def myListPrint(listP):
    if len(listP) == 0:
        print "  ", listP
    else:
        for p in listP:
            print "  ", p

    return 0   #0 => normal


#main entry point

#Needed for python manage.py shell
setup_test_environment()  #installs a template renderer (response.context)
client = Client()         #
#Contrast with python manage.py test:
#no setup_test_environment()
#django.test.TestCase class and this comes with its own client (self.client.get)


print "Display All Question"
qCount = Question.objects.count()   #0   when empty
print "  ", qCount
qObjs = Question.objects.all()      #[]  when empty
#print "  ", qObjs                   #note data type
#print "  ", qObjs.model             #note data type
#qObjs                               #note data type
#qObjs.model                         #note data type
myListPrint(qObjs)

#urlPollsSg = reverse('polls:index')
#urlPollsSg = ''
#urlPollsSg = '/'
#urlPollsSg = '/polls/blog/'
#urlPollsSg = '/polls/index/'
#urlPollsSg = '/polls/idOrder/'
#urlPollsSg = '/polls/dateOrder/'
#urlPollsSg = '/polls/'
#urlPollsSg = '/polls/2/details/'
#urlPollsSg = '/polls/2/'
#urlPollsSg = '/polls/2/results/'
#urlPollsSg = '/polls/2/vote/'

urlList= ['', '/', '/polls/blog/',
'/polls/index/', '/polls/idOrder/', '/polls/dateOrder/', '/polls/',
'/polls/2/details/', '/polls/2/', '/polls/2/results/', '/polls/2/vote/']

noOfURLsMax= len(urlList)
print "noOfURLsMax=", noOfURLsMax
k= -1
while k < (noOfURLsMax-1):
  k= k + 1
  urlPollsSg= urlList[k]
  response = client.get(urlPollsSg)
  print k, urlPollsSg, response.status_code
  #response.status_code: 200 okay #404 not-okay  #301 no last / (?)
  print response.content          #see many \n if omit print












