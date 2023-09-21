## Deploy ML model using Django
to use Django for deploying a ML/DL project
This project will focus on testing/learning Django capability
<br>
Django is based on MVT and becomes useful when multiple api integration is required.
It is a choice over flask for deployment projects with longer life cycle and spanning various teams. As it enables easy multi-feature integration

### How to Execute : 
1. start server
> python manage.py runserver <optional: specific port>
2. Navigate to Predictions page


### Django Steps :
1. to start a project
> django-admin startproject Django_2023
2. to start the app/feature
> python manage.py startapp home
3. create a python env using
> py -3.9 -m venv venv
> /venv/scripts/activate/
> pip install django
and other relevant packages
4. migrate
> python manage.py migrate
5. to run the proj
> python manage.py runserver


### References:
1. tailwind css
2. tailblock
3. get bootstrap
4. undraw co
5. colors : tailwind css colors (copy hex-code)