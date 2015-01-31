#tA01modelAPIpolls.py 

#NOTES
#Name of the table is Question, and the fields for each record
#in this table are: question_text, pub_date & itAd.
#Name of custom def routineS associated with Question are:
#was_published_recently() and choicesPub

import django
#django.setup()
print django.get_version()

#print "start of list of modules loaded"
#i = -1
#for p in sys.modules.keys():
#  i = i + 1    #i starts at 0
#  iMod = i % 4
#  if iMod == 0:
#     print p,
#  elif iMod == 1 or iMod == 2:
#     print "\t", p,
#  elif iMod == 3:
#     print "\t", p
#  else:
#     print "ERROR"
#print "\n", "end of list of modules loaded"

print django.__path__ 
import sys
for p in sys.path:
  print p
print "  "


from polls.models import Question
#TODO find out why "from polls.models import Choice" is not needed,
#even though the class Choice is used below (!?!)

#import pdb

import datetime                       #Python date/time
from django.utils import timezone     #Django date/time

def myListPrint(listP):
    if len(listP) == 0:
        print "  ", listP
    else:
        for p in listP:
            print "  ", p

    return 0   #0 => normal

def myQfieldsPrint(qP):
    print "  ", qP.id
    print "  ", qP.question_text
    print "  ", qP.pub_date
    return 0   #0 => normal



#Start of the main code
print "START\n"
#pdb.set_trace()

print "Display All Question"
qObjs = Question.objects.all()      #[]  when empty
print "  ", qObjs.model             #note data type
myListPrint(qObjs)
qCount = Question.objects.count()   #0   when empty
print "  ", qCount, "\n"

print "Display particular Questions (may or may not exist)"
ans = Question.objects.filter(id=1)
print "  ", ans.model                #note data type
myListPrint(ans)
print " "
ans = Question.objects.filter(id=5)
myListPrint(ans)
print " "
ans = Question.objects.filter(question_text__startswith='Wh')
myListPrint(ans)
print "  "
ans = Question.objects.filter(question_text__startswith='Sh')
myListPrint(ans)
listYear = [2013, 2014, 2015]
for yearVal in listYear:
   print "  "
   ans = Question.objects.filter(pub_date__year = yearVal)
   myListPrint(ans)
print " "

print "Get particular Question using id that may or may not exist"
listID = [1, 5, 35678]
for idVal in listID:
   print "idVal= ", idVal
   try:
      q = Question.objects.get(id = idVal)
   except Question.DoesNotExist:
      localErr = -1    #q not defined as no Question exist
   except:
      localErr = -9    #error (catch all)
   else:
      localErr = 0     #0 => normal otherwise error
      #dir(q) #showing it has items for Question (do in a Python Shell)
      myQfieldsPrint(q)

   print "   localErr= ", localErr
print " "

print "Get particular Question using pk that may or may not exist"
listPK = [1, 5, 35678]
for pkVal in listPK:
   print "pkVal= ", pkVal
   try:
      q = Question.objects.get(pk = pkVal)
   except Question.DoesNotExist:
      localErr = -1    #q not defined as no Question exist
   except:
      localErr = -9    #error (catch all)
   else:
      localErr = 0     #0 => normal otherwise error
      myQfieldsPrint(q)

   print "   localErr= ", localErr
print " "

print "Get a set of existing Questions using pub_date__year"
listYear = [2013, 2014, 2015]
for aYear in listYear:
   print "aYear= ", aYear
   try:
      q = Question.objects.get(pub_date__year = aYear)
   except Question.DoesNotExist:
      localErr = -1    #q not defined no Question exist in aYear
   except Question.MultipleObjectsReturned:
      localErr = -2    #more than one Question in aYear
   except:
      localErr = -9    #error (catch all)
   else:
      localErr = 0     #one Question in aYear
      myQfieldsPrint(q)

   print "   localErr= ", localErr
print " "

print "Get particular Question using id and if it exists"
print "use was_published_recently() and choicesPub()"
listID = [1,2,3,4,5,6,7,8,9,10]
for idVal in listID:
   print "idVal= ", idVal
   try:
      q = Question.objects.get(id = idVal)
   except Question.DoesNotExist:
      localErr = -1    #q not defined as no Question exist
   except:
      localErr = -9    #error (catch all)
   else:
      localErr = 0     #0 => normal otherwise error
      myQfieldsPrint(q)
      pubStateOfQuestion = q.was_published_recently()
      print "  ", pubStateOfQuestion
      noOfChoicesPub = q.choicesPub()
      print "  ", noOfChoicesPub
   print "   localErr= ", localErr
print " "

print "Get particular Question using id; and if it exists"
print "list the associated Choices"
listID = [1,2,3,4,5,6,7,8,9,10]
for idVal in listID:
   print "idVal= ", idVal
   try:
      q = Question.objects.get(id = idVal)
   except Question.DoesNotExist:
      localErr = -1    #q not defined as no Question exist
   except:
      localErr = -9    #error (catch all)
   else:
      localErr = 0     #0 => normal otherwise error
      myQfieldsPrint(q)

      choicesFor_q = q.choice_set.all()      #[] when empty
      print "  ", choicesFor_q
      #print "  ", choicesFor_q.model        #note data type
      #myListPrint(choicesFor_q)             #TODO maybe
      choicesCount = q.choice_set.count()    #0 when empty
      print "  ", choicesCount

   print "   localErr= ", localErr
print "  "


print "Create a new Question in the table and then delete the Question"
countBeforeCreateQ = Question.objects.count()
print "  ", countBeforeCreateQ
t1Now = datetime.datetime.now()
t2Now = timezone.now()
print "  ", t1Now
print "  ", t2Now
#for some reason (Django) must use t2Now for creating a new Question
q = Question(question_text="Where is it cool?", pub_date=t2Now)
q.save() #Save the Question in the database.
myQfieldsPrint(q)
print "  ", t2Now

choicesFor_q = q.choice_set.all()
print "  ", choicesFor_q
choicesCount = q.choice_set.count()
print "  ", choicesCount

countAfterCreateQ = Question.objects.count()
print "  ", countAfterCreateQ

#Delete the Question (q)

qObjs = Question.objects.all()
myListPrint(qObjs)
qCount = Question.objects.count()
print "  ", qCount

q.delete()
print "   Just Deleted the Question"

qObjs = Question.objects.all()
myListPrint(qObjs)
qCount = Question.objects.count()
print "  ", qCount
print "   "

print "Dispay a Question and if it exists display its Choices along with additional info"
listID = [1,5]
for idVal in listID:
   print "idVal= ", idVal
   try:
      q = Question.objects.get(id = idVal)
   except Question.DoesNotExist:
      localErr = -1    #q not defined as no Question exist
   except:
      localErr = -9    #error (catch all)
   else:
      localErr = 0     #q defined and have a Question
      myQfieldsPrint(q)

      choicesList = q.choice_set.all()
      print "  ", choicesList
      choicesCount = q.choice_set.count()
      print "  ", choicesCount

      #choicesList is a queryset of Choice object
      i = 0
      while i < choicesCount:
         print "  ", choicesList[i].id
         print "  ", choicesList[i].choice_text
         print "  ", choicesList[i].votes
         print "  ", choicesList[i].question_id
         print "  ", choicesList[i].question.question_text
         print "  ", choicesList[i].question.pub_date
         print "  ", choicesList[i].question.id 
         i = i + 1
      
   print "   localErr= ", localErr
print "   "

print "\nEND\n"


