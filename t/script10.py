#script10.py

import sys
for p in sys.path:
  print p
print "  "

#import django
#django.setup()
#print django.get_version()
#print django.__path__


from polls.models import Question
#TODO find out why "from polls.models import Choice" is not needed,
#even though the class Choice is used below (!?!)

print Question.was_published_recently.short_description
print dir(Question)

#print Question.question_text

#print choicesPub.short_description
