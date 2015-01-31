#tests.py
print "\nHello, this is polls/tests.py\n"

from django.test import TestCase

import datetime                     #Python date/time
from django.utils import timezone   #Django date/time
from polls.models import Question
from django.core.urlresolvers import reverse

class QuestionMethodTests(TestCase):

  def test_was_published_recently_with_futureOrPast_question(self):
    """
    was_published_recently() should return "No", "Yes " or "To be in the future!"
    for questions whose pub_date is in the past by more than 1 day, in the past by
    up to 1 day and in the future, respectively
    """
    print "test_was_published_recently_with_futureOrPast_question"
    qList = [""]
    #whenPub_NoOfDaysRelToNow = [1, -0.5, -2]
    #whenPub_NoOfDaysRelToNow = [0.5, -(23.0/24.0), -(25.0/24.0)] #1hr
    #whenPub_NoOfDaysRelToNow = [(1.0/24.0), -(1.0/24.0), -(23.0/24.0), -(25.0/24.0)]                   #1hr
    whenPub_NoOfDaysRelToNow = [(1.0/1440.0), -(1.0/1440.0), -(1439.0/1440.0), -(1441.0/1440.0)]        #1minute
    #whenPub_NoOfDaysRelToNow = [(1.0/86400.0), -(1.0/86400.0), -(86359.0/86400.0), -(86401.0/86400.0)] #1second
    expectedPub = ["To be in the future!", "Yes", "Yes", "No"]
    maxNoOfQ = len(whenPub_NoOfDaysRelToNow)
    i= -1
    while i < (maxNoOfQ - 1):
      i= i + 1
      theQuestion="Who will be here in " + str(whenPub_NoOfDaysRelToNow[i]) + " days?"
      self.createQuestionsInTestDatabase(theQuestion, whenPub_NoOfDaysRelToNow[i], qList)
      questionPubInFutureOrPast = qList[0]
      ans = questionPubInFutureOrPast.was_published_recently()
      print ans, expectedPub[i], whenPub_NoOfDaysRelToNow[i]
      self.assertEqual(ans, expectedPub[i])
    self.displayQuestionsInTestDatabase()

  def localUtilityOne(self, ipP, opP):
    """
    list (mutable) and so can be change in place,
    so, returns value to caller
    """
    opP[0] = 2 * ipP
    #print "localUtilityOne: ", ipP, opP[0], opP

  def Atest_localUtilityOne(self):
    """
    localUtilityOne() return the second parameter as twice the
    first parameter
    """
    #print "Atest_localUtilityOne"
    ipVal = 56
    Arslt = [0]   #init. mutable list of one value
    self.localUtilityOne(ipVal, Arslt)
    #print ipVal, Arslt[0], Arslt
    self.assertEqual(Arslt[0], 2*ipVal)

  def convertTo_timeNowMidnightZero(self, timeNowP, timeNowMidnightZeroP):
      timeIntervalComposite = datetime.timedelta(hours= timeNowP.hour-12,
      minutes= timeNowP.minute, seconds= timeNowP.second,
      microseconds= timeNowP.microsecond)
      print timeIntervalComposite
      timeNowMidnightZeroP[0] = timeNowP - timeIntervalComposite #zeroise h,m,s,us

      print timeNowMidnightZeroP[0], timeNowMidnightZeroP
      print timeNowP
      return 0

  def pubStatusOfQuestion(self, theQuestionP, timePublishedP, pubStatusP):
    aQuestion = Question(question_text = theQuestionP, pub_date = timePublishedP)
    #aQuestion is created, but as it is not saved it is no put in the
    #db.sqlite3 database
    pubStatusP[0] = aQuestion.was_published_recently()
    #print aQuestion.id
    #print aQuestion.question_text
    #print aQuestion.pub_date
    #print "    pubStatusOfQuestion: ", pubStatusP[0], pubStatusP, "    ",
    return 0

  def test_was_published_recently_with_any_question(self):
    """
    was_published_recently() should return "No", "Yes " or "To be in the future!"
    for questions whose pub_date is in the past by more than 1 day, in the past by
    up to 1 day and in the future, respectively
    """
    print "test_was_published_recently_with_any_question  "
    timeNow = timezone.now()
    print timeNow
    #Did not work timezone/naive/aware
    #timeNowNoon = timezone.datetime(timeNow.year, timeNow.month, timeNow.day, 12, 0, 0)
    #
    #Perhaps the published date for the Question should not be recorded in
    #polls-admin etc to such extreme values; perhaps to nearest 1 hour as opposed
    #to fractions of a second
    #
    #timeNowMidnightZero = [timeNow]
    #print "xxx", timeNowMidnightZero[0], "xxx", timeNowMidnightZero, "xxx   "
    #rtrnT = self.convertTo_timeNowMidnightZero(timeNow, timeNowMidnightZero)
    #print "xxx", timeNowMidnightZero[0], "xxx", timeNowMidnightZero, "xxx   "
    #timeNowNoon = timeNow
    #timeNowNoon = timeNowMidnightZero[0]
    #print timeNowNoon
    #
    #problem at 0 & -1 noOfDays transition variable

    #maxNoOfDays = 2.5; minNoOfDays = -2.2; decNoOfDay = 0.2;
    #maxNoOfDays = 2.4; minNoOfDays = -2.2; decNoOfDay = 0.2;

    #maxNoOfHours = 60; minNoOfHours = -60; decNoOfHours = 4 #does 0 and -24
    maxNoOfHours = 61; minNoOfHours = -61; decNoOfHours = 4  #does not do 0 and -24

    timeNowXXX = timeNow

    noOfHours = maxNoOfHours
    while noOfHours >= minNoOfHours:
      noOfHours = noOfHours - decNoOfHours
      if  noOfHours > 0:
        expectedPubStatus = "To be in the future!"
      elif noOfHours  < -24:
        expectedPubStatus = "No"
      else:
        expectedPubStatus = "Yes"

      timeInterval = datetime.timedelta(hours=noOfHours)
      timePublished = timeNowXXX + timeInterval
      theQuestion="Who will be here in " + str(noOfHours) + " hours?"
      #print timeNowXXX
      #print noOfHours
      #print timeInterval
      print timePublished
      print theQuestion
      pubStatus = [""]
      #print "xxx", pubStatus[0], "xxx", pubStatus, "xxx   "
      rtrnQ = self.pubStatusOfQuestion(theQuestion, timePublished, pubStatus)
      #print pubStatus[0], pubStatus
      print pubStatus[0], expectedPubStatus, noOfHours
      #print pubStatus[0], noOfHours
      self.assertEqual(pubStatus[0], expectedPubStatus)


  def updateAquestionWithChoices(self, qP, cP, vP):
    #print "updateAquestionWithChoices"

    #noOfChoices = qP.choice_set.count() ; print noOfChoices   #checking
    #setOfChoices = qP.choice_set.all() ; print setOfChoices   #checking
    
    #Create Choices for this Question. No need to save, as the Question has been
    #saved in the django-test database when it was created earlier. Updating of the
    #Question for the Choices happens automatically.
    noOfNewChoices = len(cP)
    #noOfNewChoicesAlso = len(vP)
    #print noOfNewChoices, noOfNewChoicesAlso
    newChoices = [""] * noOfNewChoices
    i= -1
    while i < (noOfNewChoices - 1):
      i = i + 1
      newChoices[i] = qP.choice_set.create(choice_text=cP[i], votes=vP[i])

    #noOfChoices = qP.choice_set.count() ; print noOfChoices   #checking
    #setOfChoices = qP.choice_set.all() ; print setOfChoices   #checking

    #For each Choice (newChoices[i]), obtain the Question; should all be the same Question.
    #i= -1                                     #checking
    #while i < (noOfNewChoices - 1):           #checking
    #  i = i + 1                               #checking
    #  aQ = newChoices[i].question; print aQ   #checking


  def createQuestionsInTestDatabase(self, theQuestionP, whenPub_NoOfDaysRelToNowP, qOPlistP):
    """
    Similar remarks as for: displayQuestionsInTestDatabase
    """
    #print "createQuestionsInTestDatabase"
    timeNow = timezone.now()
    timeInterval = datetime.timedelta(days=whenPub_NoOfDaysRelToNowP)
    timePub = timeNow + timeInterval
    #print timeNow
    #print whenPub_NoOfDaysRelToNowP
    #print timeInterval
    #print timePub
    #print theQuestion
    questionPub = Question(question_text = theQuestionP, pub_date = timePub)
    questionPub.save() #Save the Question in the Django-Test Database.
    qOPlistP[0] = questionPub

  def displayQuestionsInTestDatabase(self):
    """
    The Questions displayed have been created by createQuestionsInTestDatabase
    in the current session of the django-test. The Questions have been saved
    and stored in the temporary database associated with this current session of
    the django-test. Note these Questions and the database are destroyed at the
    end of the current session of the django-test.
      The Questions in the permanent database (db.sqlite3) is not involved in
    the django-test in any way.
    """
    #print "displayQuestionsInTestDatabase"
    qObjs = Question.objects.all()      #[]  when empty
    qCount = Question.objects.count()   #0   when empty
    print "Display All (", qCount, ") Questions, with Choices, in the Django-Test Database"
    if qCount <=0:
      print qObjs
    else:
      for q in qObjs:
        noOfChoices = q.choice_set.count()
        if (noOfChoices > 0):
          print q,
          setOfChoices = q.choice_set.all()
          cCount = 0
          for c in setOfChoices:
            cCount = cCount + 1
            if cCount < noOfChoices:
              print c,
            else:
              print c
        else:
          print q

  def createAsetOfQuestionsInTestDatabase(self):
    whenPub_NoOfDaysRelToNow = [0, 0, 0, 0, 0]
    theQuestion= ["Who's here?", "Who knows?", "Who helps?",  "Who does?",  "Who notices?"]
    maxNoOfQuestions = len(theQuestion)
    maxNoOfChoices = 10
    theChoices = [[""] * maxNoOfChoices] * maxNoOfQuestions
    theVotes = [[0] * maxNoOfChoices] * maxNoOfQuestions
    theChoices[0] = ["somebodyI", "nobodyI", "everybodyI"] ; theVotes[0] = [0, 0, 0]
    theChoices[1] = ["somebodyII", "nobodyII", "everybodyII"] ; theVotes[1] = [0, 0, 0]
    theChoices[2] = ["somebodyIII", "nobodyIII", "everybodyIII"] ; theVotes[2] = [0, 0, 0]
    theChoices[3] = ["somebodyIV", "nobodyIV", "everybodyIV"] ; theVotes[3] = [0, 0, 0]
    theChoices[4] = ["somebodyV", "nobodyV", "everybodyV"] ; theVotes[4] = [0, 0, 0]
    
    #print theChoices[4][0];print theChoices[4][1];print theChoices[4][2]; #checking
    #print theChoices                                                      #checking

    i= -1 ; qList = [""]
    while i < (maxNoOfQuestions - 1):
      i= i + 1
      self.createQuestionsInTestDatabase(theQuestion[i], whenPub_NoOfDaysRelToNow[i], qList)
      questionPub = qList[0]
      #print questionPub.id                 #checking
      #print questionPub.question_text      #checking 
      #print questionPub.pub_date           #checking
      self.updateAquestionWithChoices(questionPub, theChoices[i], theVotes[i])

  def develope_createAsetOfQuestionsInTestDatabase(self):
      self.createAsetOfQuestionsInTestDatabase()
      self.displayQuestionsInTestDatabase()    #checking

  def test_tB01viewResponse(self):
    """
    Display the Responses for series of Views/URLs for the Questions
    in the Django-Test Database
    """
    print "test_tB01viewResponse"

    self.createAsetOfQuestionsInTestDatabase()
    self.displayQuestionsInTestDatabase()    #checking

    #urlPollsSg = reverse('polls:index')

    urlPollsSg = [""] * 12
    urlPollsSg[0] = ''
    urlPollsSg[1] = '/'
    urlPollsSg[2] = '/polls/blog/'
    urlPollsSg[3] = '/polls/index/'
    urlPollsSg[4] = '/polls/dateOrder/'
    urlPollsSg[5] = '/polls/idOrder/'
    urlPollsSg[6] = '/polls/'
    urlPollsSg[7] = '/polls/1/details/'
    urlPollsSg[8] = '/polls/1/'
    urlPollsSg[9] = '/polls/1/results/'
    urlPollsSg[10] = '/polls/1/vote/'
    urlPollsSg[11] = '/admin/'
    maxUrlPollsSg = len(urlPollsSg)

    i=-1
    while i < (maxUrlPollsSg - 1):
      i = i + 1
      response = self.client.get(urlPollsSg[i])
      #print "Start response= ", response, "End response"
      #response                   #prints nothing I believe
      #print "check line"
      #dir(response)              #prints nothing I believe
      #response.status_code: 200 okay   404 not-okay  301 no last / (?)  302 admin (?)
      print "\n", i+1, urlPollsSg[i], response.status_code
      print response.content  #see many \n if omit print


