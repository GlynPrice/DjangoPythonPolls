# Create your models here.

from django.db import models

import datetime                     #Python date/time
from django.utils import timezone   #Django date/time

class Question(models.Model):
    question_text = models.CharField('Question Text', max_length=200)
    pub_date = models.DateTimeField('Published Date')

    #Representation of this object: Question
    # __unicode__ on Python 2, __str__ for Python 3
    def __unicode__(self):
        return self.question_text

    #Custom Method
    def was_published_recently(self):
        deltaTime = datetime.timedelta(days=1.0)
        tNow = timezone.now()
        tTransition = tNow - deltaTime
        if self.pub_date > tNow:
            valInfo = "To be in the future!"
        elif self.pub_date < tTransition:
            valInfo = "No"
        else:
            #range extremeties inclusive (0.00 & -1.00 days)
            #tTransition & tNow 
            valInfo = "Yes"
        #print "tNow= ", tNow
        #print "tTransition= ", tTransition
        #print "self.pub_date= ", self.pub_date
        #print deltaTime, deltaTime
        #print valInfo
        return valInfo
    #was_published_recently.admin_order_field = 'pub_date' #TODO: why 'pub_date' ?
    #was_published_recently.boolean = True   #valInfo is 3-way string, so cannot use this
    was_published_recently.short_description = 'Recently Published?'

    #Custom Method
    def choicesPub(self):
        noOfChoices = self.choice_set.count()
        #print "def choicesPub(self):", self.id, noOfChoices, self.question_text, self.pub_date
        if noOfChoices > 0:
           noOfChoicesSg = "Yes"
        else:
           noOfChoicesSg = "No"
        return noOfChoicesSg
    choicesPub.short_description = 'Choices Published'
    
    #Custom Method
    #def idDB(self):
    #    print "def idDB(self):", self.id, self.question_text, self.pub_date
    #    return self.id
    #idDB.admin_order_field = 'pub_date'   #TODO: why 'pub_date' ?
    #idDB.short_description = 'ID'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    #Representation of this object: Choice
    # __unicode__ on Python 2, __str__ for Python 3
    def __unicode__(self):
        return self.choice_text



