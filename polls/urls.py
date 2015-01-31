from django.conf.urls import patterns
from django.conf.urls import url
from polls import views

urlpatterns = patterns('',
    #URL /polls/blog/
    url(r'^blog/$', views.blog, name='blogs'),       #function-based view
    #URL /polls/index/
    url(r'^index/$', views.index, name='index'),     #function-based view
    #URL /polls/
    url(r'^$', views.index, name='index'),           #function-based view
    #URL /polls/idOrder/
    url(r'^idOrder/$', views.index, name='index'),   #function-based view
    #URL /polls/dateOrder
    url(r'^dateOrder/$', views.index, name='index'), #function-based view

    #URL /polls/2/details
    #url(r'^(?P<qId>\d+)/details/$', views.details, name='details'),      #function-based view
    url(r'^(?P<qId>\d+)/details/$', views.detailResults, name='details'),  #function-based view
    #URL /polls/2/
    #url(r'^(?P<qId>\d+)/$', views.details, name='details'),              #function-based view
    url(r'^(?P<qId>\d+)/$', views.detailResults, name='details'),          #function-based view

    #URL /polls/5/results/
    #url(r'^(?P<qId>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<qId>\d+)/results/$', views.detailResults, name='results'), #function-based view

    #URL /polls/5/vote/
    url(r'^(?P<qId>\d+)/vote/$', views.vote, name='vote'),   #function-based view (intended for URLaddresBox)
    #URL /polls/5/voteB/
    url(r'^(?P<qId>\d+)/voteB/$', views.vote, name='voteB'), #function-based view (intended for Button)
)


