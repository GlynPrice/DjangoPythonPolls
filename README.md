# DjangoPythonPolls

1 Feb 2015  

These are my technical notes that worked for me and things that I found interesting.  

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

Note that the localhost:8000/ view-URL is not the Django Welcome view nor a crash/error_message page, but is mapped to a function in view.py in the Django Project and not in the Polls App Project. This is quite trivial.

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

Note that inner subfolder DjangoPythonPolls for the Django-Project and the subfolder polls for the App-Polls-Project are Python packages in that they have the file `__init__.py`. This among other things allows the dot-path notation to be used when files are imported.

##RUN-UP THE POLLS APP
This app needs a Python (version 2.7.6) based virtualenv with Django (version 1.7.1). All command-lines based work below are to be done in the Terminal window.

Use `activate` to invoke the virtualenv. Use the command `which python` and `python --version` to check that the correct python is pointed to before and after doing `activate`

In the shell for python enter the following commands to check that the correct Django is installed:  

```
import django
print django.get_version()
print django.__path__

or use the following command on the command-line:

python -c "import django ; print django.get_version()
python -c "import django ; print print django.__path__
```

Set the default folder to the local repository for this app (folder that ends with DjangoPythonPolls for the above example). This subfolder should have the following files/sub-subfolders: db.sqlite3, manage.py & README.md; and DjangoPythonPolls, polls, templates & t and maybe others.

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

The Python test scripts are in the subdirectories:  
/t & /t1, below the outer Django-Project directory and polls/t.
The standard Python test script is polls/tests.py  

###METHOD1: USE STANDARD PYTHON INTERACTIVE SHELL AND IMPORT THE TEST SCRIPT

(I) DJANGO_SETTINGS_MODULE  
The the environment variable `DJANGO_SETTINGS_MODULE` needs to be set to connect to the Django software, because manage.py is not used in this test method:  
export `DJANGO_SETTINGS_MODULE`="DjangoPythonPolls.settings"  
where DjangoPythonPolls is the name of the outer Django-Project folder  

(II) SET-UP DJANGO  
As manage.py is not used in this test method `django.setup()` and `import django` has to be done either in the shell or in the test script.  

(III) PYTHONPATH  
The environment variable `PYTHONPATH` has to point to the full path of the Python test scripts. This information is used by the import statement to locate the Python test script. An example for setting-up the variable PYTHONPATH is given below (use the appropriate variation for appending):
export PYTHONPATH="/home/glyn/second2twoTraining/repro_DjangoPythonPolls/DjangoPythonPolls/t"  
where DjangoPythonPolls is the name of the outer Django-Project location/subfolder.  

(IV) STANDARD PYTHON INTERACTIVE SHELL  
Standard Python interactive shell (>>>) can be launched using:  
`python`  

At the >>> prompt for the shell, the import statement can be used to invoke the Python test script:  
`eg1               import script4`  
`eg2               import tA01modelAPIpolls`  
Note that the `reload()` function would have to be used if these scripts were edited after using the import statement while the shell is still running.  

All the attributes in these scripts are then accessible from the >>> shell prompt.  
The `dir` command/function can be used to list these attributes:  
eg1               dir(script4)  
eg2               dir(tA01modelAPIpolls)  
Use moduleName.object and print(moduleName.object) to identify type of object
Use `moduleName.object.__doc__` to try to get help

(V) DIRECTORY FOR TEST SCRIPTS IN A CONTAINER FOR PYTHON PACKAGE FILES (`__init__.py`)  
See another the section below that deals with `__init__.py` for background details. Note no need to setup PYTHONPATH.  
eg1                `import t.script4`  
eg2                `import t.tA01modelAPIpolls`  

Use quit() to exit the shell.  


###METHOD2: USE STANDARD PYTHON WITH THE TEST SCRIPT AS A PARAMETER ON THE COMMAND LINE

(I) DJANGO_SETTINGS_MODULE  
The the environment variable `DJANGO_SETTINGS_MODULE` needs to be set to connect to the Django software, because manage.py is not used in this test method:  
export `DJANGO_SETTINGS_MODULE`="DjangoPythonPolls.settings"  
where DjangoPythonPolls is the name of the outer Django-Project subfolder  

(II) SET-UP DJANGO  
As manage.py is not used in this test method, `django.setup()` and `import django` has to be done in the test script.  

(III) PYTHONPATH  
The environment variable `PYTHONPATH` has to point to the full path of the outer Django-Project directory, and NOT to the path of the test script . This information is used by the import statements for Django-App modules (eg import polls.models etc) in the Python test scripts. The subfolder of the Python test script is supplied on the command line, a shown later below. An example for setting-up the variable PYTHONPATH is given below (use the appropriate variation for appending):
export PYTHONPATH="/home/glyn/second2twoTraining/repro_DjangoPythonPolls/DjangoPythonPolls"  
where DjangoPythonPolls is the name of the outer Django-Project subfolder.  

(IV) STANDARD PYTHON INVOKED FROM THE COMMAND LINE  
To invoke a test script from the command line can be done as follows:  
eg1               `python t/script4.py`  
eg2               `python t/tA01modelAPIpolls.py`  


###METHOD3: USE DJANGO-PYTHON INTERACTIVE SHELL AND IMPORT THE TEST SCRIPT

(I) DJANGO_SETTINGS_MODULE  
The the environment variable `DJANGO_SETTINGS_MODULE` used to connect to the Django software is automatically setup, as the shell is invoked as shown below, using manage.py.

(II) SET-UP DJANGO  
As manage.py is used in this test method then this setup is done automatically  

(III) PYTHONPATH  
The environment variable `PYTHONPATH` has to point to the full path of the Python test scripts. This information is used by the import statement to locate the Python test script.  An example for setting-up the variable PYTHONPATH is given below (use the appropriate variation for appending):
export PYTHONPATH="/home/glyn/second2twoTraining/repro_DjangoPythonPolls/DjangoPythonPolls/t"  
where DjangoPythonPolls is the name of the outer Django-Project subfolder.  

DJANGO-PYTHON INTERACTIVE SHELL  
Django-Python interactive shell (>>>) can be launched using:  
`python manage.py shell`  

At the >>> prompt for the shell, the import statement can be used to invoke the Python test script:  
`eg1               import script4`  
`eg2               import tA01modelAPIpolls`  
Note that the `reload()` function would have to be used if these scripts were edited after using the import statement while the shell is still running.  

All the attributes in these scripts are then accessible from the >>> shell prompt.  

The `dir` command/function can be used to list these attributes:  
eg1               dir(script4)  
eg2               dir(tA01modelAPIpolls)  
Use moduleName.object and print(moduleName.object) to identify type of object
Use `moduleName.object.__doc__` to try to get help

(V) DIRECTORY FOR TEST SCRIPTS IN A CONTAINER FOR PYTHON PACKAGE FILES (`__init__.py`)  
See another the section below that deals with `__init__.py` for background details. Note no need to setup PYTHONPATH.  
eg1                `import t.script4`  
eg2                `import t.tA01modelAPIpolls`  

Use quit() to exit the shell.  


###METHOD4: USE DJANGO-PYTHON WITH THE TEST SCRIPT AS A PARAMETER ON THE COMMAND LINE

(I) DJANGO_SETTINGS_MODULE  
The the environment variable `DJANGO_SETTINGS_MODULE` used to connect to the Django software is automatically setup, as the shell is invoked as shown below, using manage.py.

(II) SET-UP DJANGO  
As manage.py is used in this test method, this setup is done automatically  

(III) PYTHONPATH  
The environment variable `PYTHONPATH` has to point to the full path of the Python test scripts. This information is used to locate the Python test script that is supplied as parameter on the commnd-line (see below). An example for setting-up the variable PYTHONPATH is given below (use the appropriate variation for appending):
export PYTHONPATH="/home/glyn/second2twoTraining/repro_DjangoPythonPolls/DjangoPythonPolls/polls/t"  
where DjangoPythonPolls is the name of the outer Django-Project subfolder.  

(IV) DJANGO-PYTHON INVOKED FROM THE COMMAND LINE USING THE DJANGO 'TEST' COMMAND
To invoke a test script from the command line can be done as follows:  
eg               `python manage.py test script4`  
eg               `python manage.py test tA01modelAPIpolls`  
eg               `python manage.py test myStuff321`  
The django command `test` is used.  
The name of the script does not have the .py extension.
If the script has class and def then by using the `dotted` notation, a particular section only of the test script can be used rather than the whole test script.  
eg               `python manage.py test myStuff321.Kwik.util1066okay`  

(V) DIRECTORY FOR TEST SCRIPTS IS A CONTAINER FOR PYTHON PACKAGE FILES (`__init__.py`)  
The directory path for the test script comes from the PYTHONPATH, as explained above. But by having the `__init__.py` file in the folder that contains the test script file, then the command can have the following changes:  
The directory path for the test script can appear in the command using the `dotted` notation. But this directory path is only the path relative to the current directory, that is the outer Django Project directory.  
There is no need to supply the path for the test script in PYTHONPATH.  
eg1                `python manage.py test polls.t.script4`  
eg2                `python manage.py test polls.t.tA01modelAPIpolls`  
eg3                `python manage.py test polls.t.myStuff321`  
eg4                `python manage.py test polls.t.myStuff321.Kwik.util1066okay`  
The path of these scripts relative to the outer Django Project directory is: polls.t in dotted notation & polls/t in directory notation.  

By having `__init__.py` file in a directory makes the py-script files in the directory into Python Package Files. In general these files can be imported with the relative path (relative to default, current directory used to invoke Python) supplied in dotted notation. A consequence of this is that the environment variable PYTHONPATH does not have to be used. This is quite a simplification when there are a large number of relative paths to be setup.

The default test script is tests.py in the polls directory. This python test script can be invoked as follows:  
eg1           	`python manage.py test`  
eg2           	`python manage.py test polls.tests`  
eg3           	`python manage.py test polls.tests.QuestionMethodTests.test_was_published_recently_with_futureOrPast_question`  
eg4             `python manage.py test relativePath.nameOfTestScript.NameOfClass.NameofDEF'  

Use quit() to exit the shell



