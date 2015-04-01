DTC - Django Twitter Clone
=========


 -----------------------------------------------


Description
----

This project is made as an assignment. It has minimal functionalities as similar to that of Twitter. The images are shown from 'Flickr' ( with known Flickr ID). Without registering / logging in users can search the tweets of existing users.

The requirements are

Build an app that:

* Allows anyone to go to the home page
* Has a login button on the home page
* Allows a user to login with a username and password
    * This shouldn't be http basicauth, it should allow multiple users to login with different credentials.
    * Password should be encrypted in some way, no plain text
* Has a form to create a post which displays to logged in users only, that has the following two fields:
    * message (text field). Example: A picture of my dog
    * flickr image id (text field).  Example: 5151806026
* All posts are displayed on the home page for everyone to see. Each post has:
    * the post message
    * The photo
        * Use the flickr api to get the image source url, you will need to make your own api key
        * Any size is ok, Medium-640 is a good one
    * the username
    * the timestamp
* The home page should also support json requests (aka, build an api)
    * /home or /home.html shows the html version and home.json shows the json version
    * The json request should return a list of all posts, each having the same 4 things that the html page does
* Has instructions in the readme.md about how to build the app
    * virtualenv, requirements.txt, db commands, run commands etc...



Assumptions:
-------

1. Flickr ID should be known by the user.
2. PEP-8 styling is following almost in all the places with may be some minor misses.
3. CSRF and other security related issues are not handled.
4. Session / Caching / Role based authentication are not handled.
5. Tested only in Windows ( Should ideally work in Macs as well)


Version
----
1.0

Testing the project
----

The webapp is not hosted but a demo is given @ [https://youtu.be/tLx3gf5czQ8]

Following are the ways of installing and testing the webapp.

Installation
--------
a) Git repo clone:
```sh
$ git clone https://github.com/rsubra13/dtc.git


```
b)
*Installing virtualenv*

It is a good practice to install all the packages in a virtual environment.
```sh
$ cd venv
$ virtualenv venv

New python executable in venv/bin/python
Installing setuptools, pip...done.

In Unix-Like Systems
$ source venv/bin/activate

In Windows-Systems
$ source venv/Source/activate

$ pip install -r requirements.txt

```
c) *PostGRESQL server*

* Make sure PostGRESQL is installed in your and system and it is running properly. Please create the database and use the POSTGRES connection string as given in ``config.py``

d) *Create Databases*
```sh
$ python manage.py migrate
```
Either run the above command or the commands given in ``CreateDBcommands`` file can be used to create the database manually

d) *Startup script*
```sh
$ python manage.py runserver
```
 ( Sample Project - for some educational purpose)
