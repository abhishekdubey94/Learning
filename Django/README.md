Virtual Environment:
A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them.
	For python 3.3 and above
		Command ->>>> python3.8 -m venv .
To Activate - > source <LOCATION_OF_ACTIVATE>
django-admin 
Create a project
django-admin startproject <PROJECT_NAME> <LOCATION>
To start the server
Go to the project location
Python manage.py runserver
To sync databases
Python manage.py migrate
To create superuser
python manage.py createsuperuser
To create custom apps
python manage.py startapp <Name_Of_The_Component>
To create a model
Use models.py in the created component
Create a class and inherit the properties from models.Model
Add the component name in the INSTALLED_APPS section of settings.py
Whenever any change is made in models.py of any component, run command makemigrations and migration
To map database with model,
Go to admin.py of respective component
from .models import <MODEL_CLASS>
.models above represent the models.py. It is a relative import
admin.site.register(<MODEL_CLASS>)
Using python shell in virtualenv for adding data in database
python manage.py shell
To get all the objects in the database <MODEL_NAME>.objects.all()
To create an object in the database <MODEL_NAME>.objects.create()
To Create Custom pages or views
Define a method in views.py of the component
Import HttpResponse class
Return HttpResponse(<HTML>)
Now mention the view in the python file mentioned in the “ROOT_URLCONF” in the settings.py.
Add an import:  from my_app import views
Add a URL to urlpatterns:  path('', views.home, name='home')
 
To add custom pages with html file
Create a folder templates or any other name.
Mention this folder name in the “Templates” of the settings.py
Add html files in the folder
Add the view method with arguments as def home_view(request,*args,**kwargs)
In the views, return render(request,”HTML_PAGE_NAME”,{})

