from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    #URL localhost:8000/admin/
    url(r'^admin/', include(admin.site.urls)),

    #URL localhost:8000
    url(r'^$', 'DjangoPythonPolls.views.homeDjangoProject', name='homeDjangoProject'),

    #URL localhost:8000/blog/  #sent for further processing
    #url(r'^blog/', include('polls.urls', namespace="polls")),

    #These sent for further processing
    #URL localhost:8000/polls/blog/  
    #URL localhost:8000/polls/
    #URL localhost:8000/polls/index/
    #URL localhost:8000/polls/idOrder
    #URL localhost:8000/polls/dateOrder
    #URL localhost:8000/polls/1/details
    #URL localhost:8000/polls/1/
    #URL localhost:8000/polls/1/results/
    #URL localhost:8000/polls/1/vote
    url(r'^polls/', include('polls.urls', namespace="polls")),

    #URL localhost:8000      further notes
    #Comment the above two url lines (url(r'^$',  &  url(r'^polls/',)
    #to get Django Welcome page instead
    #UNComment the above two url lines to get home page
    #Comment only one url line with url(r'^$', to get: Page not found (404)
    #Comment only one url line with url(r'^polls/', to get home page (may be silly, but true)
)
