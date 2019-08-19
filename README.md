# Python-Django-Api-Using-JSON-Response
We can write rest api using python django rest framework using json response method

# from the above repository https://github.com/bhushanzade/Python-Django-Rest-API-Demo

You can see demo how we start django rest framework and how to create model and views for creating tables and request url

In this example we are going to create custom rest api without using rest framework

in this repository check models.py file for creating table under the nosql database in python

and views.py file for creating json response data for get request

admin.py file is used to register model under admin

urls.py is used to create api urls for testing web api

you caan test on browser also

e.g. 

# Get by ID request
127.0.0.1:8000/api/getEmployeeByID/1
in this we get the id 1 response in json format
this will generating this urls using 2 type
1) path('api/getEmployeeByID/<int:id>',views.GetEmployeeByID.as_view()),
2) url(r'^api/getEmployeeByID/(?P<id>\d+)/$',views.GetEmployeeByID.as_view()),
  
  (?P<id>\d+)  This is syntax for taking id from the user
  <int:id> this is also similar work like above

# Get all data

127.0.0.8000/api/getallemployee
This will give us all employee data from employee table.


# Thaank you !!!
