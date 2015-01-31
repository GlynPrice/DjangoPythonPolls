# DjangoPythonPolls

28 Jan 2015  

These are my technical notes that worked for me and that I found interesting.  

All command-lines based work below are to be done in the Terminal window.  

##INTRODUCTION
This simple example of Django-Python code was developed under Ubuntu 14.04 LTS (installed alongside MS windows 7). The Python inherent in the Ubuntu system (version 2.7.6) was used when creating a virtualenv, and the Django software package version 1.7.1 was installed in this virtualenv.  

The views for this app are function-based rather than class-based.

##USER NOTES
This Django-Python code is based on the tutorial and sample code on the docs.djangoproject.com/en/1.7 (polls app) website. The views for this app are function-based, and the view-URLs are:  
localhost:8000/  
localhost:8000/admin/  
localhost:8000/polls/blog/  

localhost:8000/polls/index/  
localhost:8000/polls/idOrder/  
localhost:8000/polls/dateOrder/  
localhost:8000/polls/  

localhost:8000/polls/2/details/  
localhost:8000/polls/2/  

localhost:8000/polls/2/results/  
localhost:8000/polls/2/vote/  

Note that the localhost:8000/ view-URL is not the Django Welcome view nor a crash/error_message page, but is mapped to a function in view.py in the polls app. This is quite trivial.

The localhost:8000/admin view-URL is the Django admin login facility and displays the Questions already entered into this app. Associated with each Question are a set of Choices. The Questions can have the following characteristics:  
1. published date that is in the future or  
2. published date that is in the past by up to 1 day (recently published) or  
3. published date that is in the past by more than 1 day  
4. no choices assigned or  
5. choices already setup  

The forms in the Django admin pages lists the above characteristics of the Questions as well as having facilities for adding, editing and deleting the Questions and Choices.

To do this editing, invoke the admin-view, select the Polls Question list, then click accurately on the value of id number associated with a particular Question. A new page is produced with the text boxes for all the fields for the particular Question. These fields/text-boxes can be edited; click on the Save button to return to the list of Questions. The adding and deleting facilities are quite straightforward.

The URL-view ending in polls/blog/ is trivial.

Consider the view-URLs ending in: polls/index/, polls/idOrder/, polls/dateOrder/ and polls/. These display the Questions already in this app, but omits the following Questions:  
1. for future publication  
2. have no assigned Choices yet  
3. that have been deleted from the database.  

Note that each Question listed on the page is a link and can be clicked to invoke the voting/details page for the selected Question.

The Questions can be listed in order of the Question id or Question published-date. The default is in published date order. Note that the id of the Questions that have been deleted can be inferred by using the Django-admin forms/views and organising the Question in id order. Missing id numbers are the id values of the deleted Questions. The polls/index/ etc views do show the Question id but the id values can be missing for other reasons (see above).

Consider the view-URLs ending in: polls/2/details/ and polls/2/. These display the Choices for the Question with an id value of 2. The parameter 2 can be any other number provided it:  
1. does not correspond to a deleted Question  
2. is not a id value that is not yet used in the Django-Admin/database  
3. does not correspond to a Question with a future published date  
4. does not correspond to a Question with no assigned choices  

The Choices are listed on the page with radio buttons for selection; also there is a button on the page to vote for your choice.

Consider the view-URL ending in: polls/2/results/. This displays the Choices for the Question with an id value of 2 with the current accumulative (all users of the app) voting talley for each Choice . The defintion of this parameter 2 is the same as described above.  

The voting talley for each Choice and for each Question can be zeroised by using the general editing facility in the Django-Admin forms. To do this editing, invoke the admin-view, select the Polls Question list, then click accurately on the value of id number associated with a particular Question. Then a new page is produced with the text boxes for all the fields for the particular Question. The fields for the voting tallies can be edited, and so can any of the other fields. Then click on the Save button to return to the list of Questions.  

Consider the view-URL ending in: polls/2/vote/. This displays the Choices for the Question with an id value of 2 (2 has the same definition as above) and the voting facility. This view_URL is simply a URL-based method to invoke the voting facility in addition to via a voting button in other pages (see above).  

##INSTALLATION OF THE POLLS APP
Create a folder with any name of your choice probably in the home directory on your Ubuntu system. It is to be the local repository for this app.  

Use the **git clone** command to transfer a copy of the files for this app to your local repository. This command needs the URL of the remote repository for this app, that is obtainable from the GitHub website (github.com): right-sidebar and `HTTPS clone URL`. An example of this command is:  

git clone https://github.com/GlynPrice/DjangoPythonPolls.git  

This command creates a subfolder (DjangoPythonPolls for the above example) with the set of files for this polls app and the git related files/subfiles. Note that this DjangoPythonPolls is the outer subfolder with this name. There is an inner subfolder with this name that is the Django-Project folder, that is alongside the polls subfolder. If you need to change the name DjangoPythonPolls to something else remember there are quite a number of places in this app that would need editing (use `grep -ir command` to help finding them). Also note that the name of the github remote repository for this app is also, DjangoPythonPolls.  

Note that inner subfolder DjangoPythonPolls for the Django-Project and the subfolder polls for the App-Polls-Project are Python package in that they have the file __init__.py. This among other things allows the dot-path notation to be used when files are imported.

##RUN-UP THE POLLS APP
This app needs a Python (version 2.7.6) based virtualenv with Django (version 1.7.1). All command-lines based work below are to be done in the Terminal window.

Use `activate` to invoke the virtualenv. Use the command `which python` and `python --version` to check that the correct python is pointed to before and after doing `activate`

In the shell for python enter the following commands to check that the correct Django is installed:  

```
import django
print django.get_version()
print django.__path__

or use the following command:

python -c "import django ; print django.get_version()
python -c "import django ; print print django.__path__
```

Set the default folder to the local repository for this app (folder that ends with DjangoPythonPolls for the above example). This subfolder should have the following files/sub-subfolders: db.sqlite3, manage.py & README; and DjangoPythonPolls, polls, templates & t and maybe others.

Invoke the server for the app as follows:  

`python manage.py runserver`  

Invoke a browser (eg Mozilla  Firefox) and enter the views_URL in the address box. For further details see the **User Notes** above.  

After finishing with the polls app: exit the browser, ctrlC on the Terminal to exit the server (apps/Django) and use `deactivate` to revert back to the standard environment.

To check the database use the following commands at the Terminal window. These commands can be done in virtualenv or standard environment.  

```
sqlite3 db.sqlite3
.tables
.headers on
select * from polls_question;
select * from polls_choice;
.quit
```

##TESTING METHODS

1. use cd to set the default directory to the outer Django-Project directory (where manage.py etc are located)  
2. set the environment variable PS1, if the prompt at the terminal is too long, eg export PS1="g_ "  
3. switch to virtualenv using `activate` if the Django-Python software has been installed in the virtualenv  

The Python test scripts used for testing would in general be Django based (import django, import from the django app, etc), but non-Django Python scripts could also be used but would probably be of limited value.  

The Python test scripts are in the subdirectory, call t/, below the outer Django-Project directory.TODO  


###METHOD1: USE STANDARD PYTHON INTERACTIVE SHELL AND IMPORT THE TEST SCRIPT

DJANGO_SETTINGS_MODULE
The the environment variable `DJANGO_SETTINGS_MODULE` needs to be set to connect to the Django software because manage.py is not used in this test method:  
export DJANGO_SETTINGS_MODULE="DjangoPythonPolls.settings"  
where DjangoPythonPolls is the name of the outer Django-Project location/subfolder  

SET-UP DJANGO  
As manage.py is not used in this test method TODO  

PYTHONPATH
The environment variable `PYTHONPATH` has to point to the full path of the Python test scripts. This information is used by the import statement to locate the Python test script. For example:  
export PYTHONPATH="/home/glyn/second2twoTraining/repro_DjangoPythonPolls/DjangoPythonPolls/t"  
where DjangoPythonPolls is the name of the outer Django-Project location/subfolder.  

STANDARD PYTHON INTERACTIVE SHELL
Standard Python interactive shell (>>>) can be launched using: `python`  

At the >>> prompt for the shell the import statement can be used to invoke the Python test script:  
`eg1               import script4`  
`eg2               import tA01modelAPIpolls`  
Note that the `reload()` function would have to be used if these scripts were edited after using the import statement while the shell is still running.  

All the attributes in these scripts are then accessible from the >>> shell prompt.  
The `dir` command/function can be used to list these attributes:  
eg1               dir(script4)  
eg2               dir(tA01modelAPIpolls)  
Use object and print(object) to identify type of object
Use obj.__doc__ to get help

Use quit() to exit >>>  


###METHOD2: USE STANDARD PYTHON WITH THE TEST SCRIPT AS A PARAMETER ON THE COMMAND LINE

DJANGO_SETTINGS_MODULE
The the environment variable `DJANGO_SETTINGS_MODULE` needs to be set to connect to the Django software because manage.py is not used in this test method:  
export DJANGO_SETTINGS_MODULE="DjangoPythonPolls.settings"  
where DjangoPythonPolls is the name of the outer Django-Project location/subfolder  

SET-UP DJANGO  
As manage.py is not used in this test method TODO  

PYTHONPATH  
The environment variable `PYTHONPATH` has to point to the full path of the Django-Project directory, and NOT to the path of the test script . This information is used by the import statements for Django-App module (eg import polls.models etc) in the Python test scripts. The location-subfolder of the Python test script is supplied on the command line, a shown later below. An example for setting-up the variable PYTHONPATH is given below:

STANDARD PYTHON INVOKED FROM THE COMMAND LINE
export PYTHONPATH="/home/glyn/second2twoTraining/repro_DjangoPythonPolls/DjangoPythonPolls"  
where DjangoPythonPolls is the name of the outer Django-Project location/subfolder.  

To invoke a test script from the command line can be done as follows:  
eg1               `python t/script4`  
eg2               `python t/tA01modelAPIpolls`  


###METHOD3: USE DJANGO-PYTHON INTERACTIVE SHELL AND IMPORT THE TEST SCRIPT

DJANGO_SETTINGS_MODULE
The the environment variable `DJANGO_SETTINGS_MODULE` to connect to the Django software is automatically setup, as the shell is invoked as shown below, using manage.py.

SET-UP DJANGO  
As manage.py is used in this test method then this setup is done automatically  

PYTHONPATH
The environment variable `PYTHONPATH` has to point to the full path of the Python test scripts. This information is used by the import statement to locate the Python test script. For example:  
export PYTHONPATH="/home/glyn/second2twoTraining/repro_DjangoPythonPolls/DjangoPythonPolls/t"  
where DjangoPythonPolls is the name of the outer Django-Project location/subfolder.  

DJANGO-PYTHON INTERACTIVE SHELL
Django-Python interactive shell (>>>) can be launched using: `python manage.py shell`  

At the >>> prompt for the shell the import statement can be used to invoke the Python test script:  
`eg1               import script4`  
`eg2               import tA01modelAPIpolls`  
Note that the `reload()` function would have to be used if these scripts were edited after using the import statement while the shell is still running.  

All the attributes in these scripts are then accessible from the >>> shell prompt.  

The `dir` command/function can be used to list these attributes:  
eg1               dir(script4)  
eg2               dir(tA01modelAPIpolls)  
Use object and print(object) to identify type of object
Use obj.__doc__ to get help

Use quit() to exit >>>

###METHOD4: USE DJANGO-PYTHON WITH THE TEST SCRIPT AS A PARAMETER ON THE COMMAND LINE

DJANGO_SETTINGS_MODULE
The the environment variable `DJANGO_SETTINGS_MODULE` to connect to the Django software is automatically setup, as the shell is invoked as shown below, using manage.py.

SET-UP DJANGO  
As manage.py is used in this test method then this setup is done automatically  

PYTHONPATH
TODO

DJANGO-PYTHON PYTHON INVOKED FROM THE COMMAND LINE USING THE DJANGO 'TEST' COMMAND
To invoke a test script from the command line can be done as follows:  
eg1               `python manage.py test      TODO             t/script4`  
eg2               `python manage.py test      TODO        t/tA01modelAPIpolls`  




ooooooooooo ooooooo
import django and django.setup()  

SET-UP DJANGO  
The statement, import django, must be in all of the Django-Python test scripts. But when non-Django Python (not using manage.py) is used, ie shell invoked with only python or python invoked on the command line, then the following Django setup is required to connect to the Django software installation:

django.setup()         #a statement in the Django-Python test scripts

__init__.py	in sub-sub-folders
import t.nameOfTestScriptWithoutPYextension
python manage.py test polls.tests.NameOfClass.NameofDEF


ooooooooooooooooooo


