from django.http import HttpResponse
from polls.models import Question
from polls.models import Choice
from django.utils import timezone
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def blog(request):
    #First parameter, request, is a HttpRequest object setup by Django
    #The other parameters, if any, are the captured values from the
    #regular expression in the URLconf;
    #Simple captures: values are passed as positional arguments and
    #Named captures: values are passed as keyword arguments.
    return HttpResponse("You're at the polls blogs page.")

#def index(request):
#    return HttpResponse("You're at the polls index page.")
def index(request):
    """
    Return all of the published questions, but excluding
    (a) those that have been deleted from the database,
    (b) those to be published in the future and
    (c) those that do not have assigned choices
    """
    ansURL = request.path_info
    #print "ansURL= ", ansURL

    #print "Display All Question"
    #qCount = Question.objects.count()   #0   when empty
    #print "  ", qCount
    #qObjs = Question.objects.all()      #[]  when empty
    #print "  ", qObjs                   #note data type

    dateOrderLoc = ansURL.find('dateOrder')   #not dependent on hardcoded URL
    if dateOrderLoc >= 0:                     #eg1 /polls/dateOrder/ eg2 /polls/idOrder/
       dateOrderFlg = True
    else:
       dateOrderFlg = False
    idOrderLoc = ansURL.find('idOrder')
    if idOrderLoc >= 0:
       idOrderFlg = True
    else:
       idOrderFlg = False
    #print dateOrderFlg, idOrderFlg

    #Questions that have been deleted from the database are automatically excluded.
    #The id associated with a deleted question is not re-used though.

    #FILTER QUESTIONS THAT ARE FUTURE QUESTIONS
    if (dateOrderFlg == True) and (idOrderFlg == False):
      listOfQuestions = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[0:]
      numQuestionsNoFuture = len(listOfQuestions)
      orderType = "date"
    elif (idOrderFlg == True) and (dateOrderFlg == False):
      listOfQuestions = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-id')[0:]
      numQuestionsNoFuture = len(listOfQuestions)
      orderType = "id"
    else:
      listOfQuestions = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[0:]
      numQuestionsNoFuture = len(listOfQuestions)
      orderType = "date"

    numQuestionsMax = Question.objects.count()
    #print numQuestionsMax, numQuestionsNoFuture, listOfQuestions

    #i = 0
    #while i < numQuestionsNoFuture and i >= 0:
    #  res = listOfQuestions[i].choice_set.count()
    #  print i, listOfQuestions[i].id, listOfQuestions[i].question_text, res
    #  i += 1   #i ranges from 0 to (numQuestionsNoFuture-1)

    #FILTER QUESTIONS THAT HAVE NO ASSIGNED CHOICES
    #print "\n"
    i = 0 ; numQuestionsNoChoices = numQuestionsNoFuture
    while i < numQuestionsNoChoices and i >= 0:
      #listOfQuestions is a QuerySet and not a plain Python List
      res = listOfQuestions[i].choice_set.count()
      #print i, listOfQuestions[i].id, listOfQuestions[i].question_text, res,
      if res <= 0:
         id_correspond_i = listOfQuestions[i].id
         reducedListOfQuestions = listOfQuestions.exclude(pk=id_correspond_i)
         listOfQuestions = reducedListOfQuestions
         numQuestionsNoChoices -= 1
         #leave i unchanged
         #print "removeItem", numQuestionsNoChoices, i
      else:
         #leave numQuestionsNoChoices unchanged
         i += 1   #i ranges from 0 to (numQuestionsNoChoices-1)
         #print "leaveItem", numQuestionsNoChoices, i
      #if i > 20 or i < 0:    #TODO: check if this infinite loop protection is worthwhile
      #   print "Inconsistency Error", numQuestionsNoChoices, i
      #   break
         
    numNoFuture = numQuestionsMax - numQuestionsNoFuture
    numNoChoices = numQuestionsNoFuture - numQuestionsNoChoices
    numQuestions = numQuestionsNoChoices
         
    context = {'listOfQuestions': listOfQuestions, 'numQuestions' : numQuestions,
               'numNoFuture' : numNoFuture, 'numNoChoices' : numNoChoices,
               'orderType' : orderType}
    print "polls/views.py numQuestions = ", numQuestions
    return render(request, 'polls/index.html', context)

#def details(request, qId):
#    #print "qId= ", qId
#    return HttpResponse("You're looking at question (id= %s)." % qId)

#def results(request, qId):
#    response = "You're looking at the results of question (id= %s)"
#    return HttpResponse(response % qId)

#def detailResults(request, qId):
#    ansURL = request.path_info
#    print "ansURL= ", ansURL
#    return HttpResponse("You're looking at question or results of question (id= %s)." % qId)

def detailResults(request, qId):
    #IDENTIFY IF URL-COMMAND IS: details or results 
    ansURL = request.path_info
    #print "ansURL= ", ansURL
    detailFlg = False ; resultsFlg = False #init, just in case

    detailLoc = ansURL.find('details')     #not dependent on hardcoded URL
    if detailLoc >= 0:                     #eg /polls/6/detail/
       detailFlg = True
    else:
       detailFlg = False
    resultsLoc = ansURL.find('results')    #eg /polls/6/results
    if resultsLoc >= 0:
       resultsFlg = True
    else:
       resultsFlg = False
    print detailFlg, resultsFlg

    if detailFlg == False and resultsFlg == False :
        #eg /polls/6/
        detailFlg=True ; resultsFlg=False
    elif detailFlg==True and resultsFlg==True :
        #this is impossible, but just in case(jic)
        return HttpResponse("Error1: ansURL= %s is perhaps ambiguious." % ansURL)

    #CHECK IF QUESTION IS A FUTURE QUESTION, HAS NO ASSIGNED CHOICES OR DOES NOT EXIST
    try:
        question = Question.objects.get(pk=qId)

        ans = question.was_published_recently()
        #print "ans= ", ans
        if (ans == "To be in the future!"):
            return HttpResponse("Question (id= %s) is to be published sometime in the future." % qId)

        noOfChoices = question.choice_set.count()
        #print qId, question.id, question.pub_date, question.question_text, noOfChoices
        if noOfChoices <= 0:
           return HttpResponse("Question (id= %s) yet to have choices published." % qId)
    except Question.DoesNotExist:
        #raise Http404
        return HttpResponse("Question (id= %s) has been deleted or never inserted from/in the database." % qId)

    #RENDER URL-COMMAND: details or results 
    error_message = ""
    if detailFlg==True and resultsFlg==False:
       return render(request, 'polls/detail.html', {'q': question, 'error_message': error_message})
    elif resultsFlg==True and detailFlg==False:
       return render(request, 'polls/results.html', {'q': question, 'error_message': error_message})
    else:
       #(detailFlg=False and resultsFlg=False)      or        (detailFlg=True and resultsFlg=True)
       return HttpResponse("Error2: ansURL= %s is ambiguious." % ansURL)

#def vote(request, qId):
#    return HttpResponse("You're voting on question (id= %s)." % qId)

def vote(request, qId):
    #q = get_object_or_404(Question, pk=qId)
    #print qId, q.id, q.pub_date, q.question_text

    #CHECK IF QUESTION IS A FUTURE QUESTION, HAS NO ASSIGNED CHOICES OR DOES NOT EXIST
    try:
        q = Question.objects.get(pk=qId)
        noOfChoices = q.choice_set.count()
        #print qId, q.id, q.pub_date, q.question_text, noOfChoices
        if noOfChoices <= 0:
           return HttpResponse("Question (id= %s) yet to have choices published." % qId)
    except Question.DoesNotExist:
        #raise Http404
        return HttpResponse("Question (id= %s) has been deleted or never inserted from/in the database." % qId)

    ans = q.was_published_recently()
    #print "ans= ", ans
    if (ans == "To be in the future!"):
      return HttpResponse("Question (id= %s) is to be published sometime in the future." % qId)

    #IDENTIFY IF URL-COMMAND IS: vote or voteB 
    ansURL = request.path_info
    #print "ansURL= ", ansURL
    voteFlg = False ; voteBFlg = False   #init, just in case

    voteLoc = ansURL.find('vote')        #not dependent on hardcoded URL
    if voteLoc >= 0:                     #eg /polls/6/vote/    from URLaddressBox
       voteFlg = True
    else:
       voteFlg = False
    voteBLoc = ansURL.find('voteB')      #eg /polls/6/voteB/   from Button (detail.html)
    if voteBLoc >= 0:
       voteBFlg = True
    else:
       voteBFlg = False
    #print voteFlg, voteBFlg

    if voteFlg == True and voteBFlg == False :
       #it is vote
       voteFlg == True   #overkill
       voteBFlg == False #overkill
    elif voteFlg == True and voteBFlg == True :
       #it is voteB
       voteFlg = False
       voteBFlg = True  #overkill
    elif voteFlg == False and voteBFlg == False :
       #this is impossible, but just in case(jic)
       return HttpResponse("Error1 (vote): ansURL= %s is perhaps ambiguious." % ansURL)       
    elif voteFlg == False and voteBFlg == True :
       #this is impossible, but just in case(jic)
       return HttpResponse("Error2 (vote): ansURL= %s is perhaps ambiguious." % ansURL)
    #print voteFlg, voteBFlg  

    if voteFlg == True and voteBFlg == False:
       #From the URLaddressBox      /polls/7/vote
       #Display the question voting form, as it is not there
       #Form would be there for voteBFlg == True
       #Invoked by a button(s) from polls/detail.html and indirectly from polls/results.html
       return render(request, 'polls/detail.html', {
           'q': q,
           'error_message': "",
       })

    try:
       pk=request.POST['choice']
       #print "pk= ", pk
       selected_choice = q.choice_set.get(pk=request.POST['choice'])
       #print "selected_choice (try) = ", selected_choice
    except (KeyError, Choice.DoesNotExist):
       #print "selected_choice (except) = none"
       #Redisplay the question voting form, as the user has not entered a choice
       return render(request, 'polls/detail.html', {
           'q': q,
           'error_message': "Error: You didn't select a choice for this question.",
       })
    else:
       #print "selected_choice (else) = ", selected_choice
       selected_choice.votes += 1
       selected_choice.save()
       #Always return a HttpResponseRedirect after successfully dealing
       #with POST data. This prevents data from being posted twice if a
       #user hits the Back button.
       theURLforResults= reverse('polls:results', args=(q.id,))
       #print "theURLforResults = ", theURLforResults
       return HttpResponseRedirect(theURLforResults)



