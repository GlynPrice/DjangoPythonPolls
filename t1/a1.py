#a1.py

import datetime                     #Python date/time
from django.utils import timezone   #Django date/time
#import sys
from polls.models import Question

#currentQuestions = Question.objects.all()
#for q in currentQuestions:
#  print q.id, q.question_text, q.pub_date
#
#for p in sys.path:
#  print p
#
timeNow = timezone.now()

i=3.25
while i > -3:
  i = i - 0.25
  noOfDays = i
  timeInterval = datetime.timedelta(days=noOfDays)
  timeFuture = timeNow + timeInterval
  #print timeNow
  #print timeInterval
  #print timeFuture
  questionPubInFuture = Question(question_text="Who will be here in 10 days?",
  pub_date = timeFuture)
  #print questionPubInFuture.id
  #print questionPubInFuture.question_text
  #print questionPubInFuture.pub_date

  ans = questionPubInFuture.was_published_recently()
  print i, ans



