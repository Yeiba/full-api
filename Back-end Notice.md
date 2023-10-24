# Mazad Multivendor Ecommerce Website

=================================

## Setup Project and creating database models

==============================================

1.  Python
2.  Install virtual Enviroment - pip3 install virtualenv
3.  Create virtual Enviroment - python3 -m venv env
4.  Activate virtual Enviroment - source env/bin/activate {deactivate}
5.  Install django - pip3 install django
6.  Create django project - django-admin startproject backend_api
7.  Run django project - python3 manage.py runserver
8.  Install PostgreSQL -Interactive installer by EDB {www.postgresql.com}
9.  install package to contact django to a db - pip3 install psycopg2-binary
10. django rest framework - pip3 install djangorestframework
11. Create app - python3 manage.py startapp main
    {
    admin.py 'handle admin tools',
    apps.py 'handle the by default section for this particular app'
    **init**.py 'defines this app as a module'
    migrations 'create migrations and migrate in the db'
    models.pu 'create models'
    tests.py
    views.py 'responsible for sending the models data to the tempaltes'
    }
12. in the 'main/models.py' create our models {Seller model, Product Category model, Product model} and migrate it to db tabels
13. python3 manage.py migrate
14. python3 manage.py makemigrations {whenever change in the modle run this command}
15. python3 manage.py migrate {after change in the modle run command to migrate changes to sql tables}

## Create Django API Serializer, Views & urls

==============================================

Attach our models from '/main/models.py' to the rest_framework and transfer our data as JSON data to api

1.  in particular app 'main/' create urls.py
2.  in 'backend_api/urls.py' imclude 'main/urls.py'
3.  in particular app 'main/' create serializer.py {responsibe for transferming the models data in db to JSON data}
4.  in 'main/views.py' import serializer {what kind of data we will send to show}
5.  by using {generics.ListAPIView} in 'main/views.py' it will return that data as list
    Summary: when we open api/ then this will include main/urls.py it's by defualt it will open the vendor list as JSON data {views getting data from serializer and serializer getting data from models}
6.  create admin panel - python3 manage.py createsuperuser
7.  in 'main/admin.py' add our models to the admin panels

## Vendor List & Detail API with Login Auth

============================================

1.  in 'main/views.py' import permissions {add authentication to vendor list in view level permission}
2.  in 'backend_api/settings' {add rest_framework for app level permissions}
    Summary: how we add permission on view level and on app level
3.  create vendor list api {depth means it will go to one depth in related model}
    Summary: whenever we went any data from the server then we need the authentication

## Product api for showing listing & detail

============================================

1.  in 'main/admin.py' add product and product category to admin register
2.  in 'main/models.py' attached the product category and the vendor and the product
3.  in 'main/serializers.py' create serializer for product and the vendor
4.  in 'main/views.py' create views for product and the vendor
5.  in 'main/urls.py' create urls for product and the vendor

## JWT(JSON Web Token) authentication with Django Rest {token authentication}

==============================================================================

    introduction: whenever we went any data from the server then we need the authentication, we have to make ti more secure so on every request i will send a username and password, with a help of JWT token {JSON web token}
    JWT {JSON web token}: is stateless, stateless it's means it is not save anything on the server, first it will generate the token according to the username and password, the token it has some life (like 10 minutes), whenever toke life expired we refresh our token to generate another token, there are tow type of token in this (access and refresh), access token to fetch the data and refresh token to generate another token whenever it's expired.

1.  install jwt - pip3 install djangorestframework-simplejwt
2.  in 'backend_api/settings.py' add JWT classes in REST_FRAMEWORK
3.  in 'backend_api/urls.py' add views as jwt_views for rest_framework_simplejwt
4.  install (http client) httpie third-party to send post request - brew install httpie

## Customer, Order & OrderItems model, Customer API

=====================================================

    introduction: customer model responsible for saving the customer data. and order model responsible for order data with customer products.
    create api for customer and order and order items.

1.  in 'main/models.py' attached the customer and order and order items
2.  in 'main/serializers.py' create serializer for customer and order and order items
3.  in 'main/views.py' create views for customer and order and order items
4.  in 'main/urls.py' create urls for customer and order and order items
5.  in 'main/admin.py' register the customer and order and order items

## Django Rest Framework Pagination

====================================

## Viewsets & Routers for customer address

============================================

    introduction: ViewSet responsible for making all the actions in single URL

1.  in 'main/models.py' attached the customer address model
2.  in 'main/serializers.py' create serializer for customer address model
3.  in 'main/views.py' create views for customer address model
4.  in 'main/urls.py' create urls for customer address model
5.  in 'main/admin.py' register the customer address model

## Product Rating and Reviews

=============================
