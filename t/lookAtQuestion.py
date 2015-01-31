#lookAtQuestion.py
import polls.models

print polls.models.Question

q1 = polls.models.Question()
print "It is: ", q1.question_text
print "It is: ", q1.pub_date 

q1.question_text = "rubbish"
print "It is: ", q1

print q1.__unicode__()

print polls.models.Question.objects.all()
