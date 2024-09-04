# This SCRATCHPAD exists solely for the pupose of evidence of the journey and path i have taken in working on this.

It contents are prune to continuous 

## Setting up CMS

## Setting up CMS

## Setting up App

## Setting up Store

-- Building shop

## Setting up Wiki

#### Creating a New Project

´´´´
lektor quickstart
´´´´

Running your Project
´´´´
$ cd yourproject
 $ lektor server
´´´´

$ lektor quickstart
Lektor Quickstart
=================

This wizard will generate a
new basic project with some
sensible defaults for getting
started quickly.  We just need
to go through a few questions
so that the project is set up
correctly for you.

Step 1:
| A project needs a name.  The
| name is primarily used for  
| the admin UI and some other
| places to refer to your
| project to not get confused
| if multiple projects exist.
| You can change this at any  
| later point.
> Project Name: OASSP WIKI

Step 2:
| Your name.  This is used in
| a few places in the default
| template to refer to in the
| default copyright messages.
> Author Name [U]: KIYINI JOSE
PH BALAMAZZE

Step 3:
| This is the path where the  
| project will be located.
| You can move a project
| around later if you do not  
| like the path.  If you
| provide a relative path it  
| will be relative to the
| working directory.
> Project Path [D:\BaselBuilds\projects\OASSPHome\OASSPHome\wiki\OASSP WIKI]:

Step 4:
| Do you want to generate a
| basic blog module?  If you  
| enable this the models for a
| very basic blog will be
| generated.
> Add Basic Blog [Y/n]: Y

C:\Users\U\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\lektor\quickstart.py:228: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  "today": datetime.utcnow().strftime("%Y-%m-%d"),

U@X1 MINGW64 /d/BaselBuilds/projects/OASSPHome/OASSPHome/wiki (master)
$

### Admin

#### Building

Project path: D:\BaselBuilds\projects\OASSPHome\OASSPHome\wiki\OASSP WIKI\OASSP WIKI.lektorproject

* Output path: C:\Users\U\AppData\Local\Lektor\Cache\builds\f21f31afdc8f757fde1d257d6b687b2f  

#

 $ lektor server

* Project path: D:\BaselBuilds\projects\OASSPHome\OASSPHome\wiki\OASSP WIKI\OASSP WIKI.lektorproject
* Output path: C:\Users\U\AppData\Local\Lektor\Cache\builds\f21f31afdc8f757fde1d257d6b687b2f
Started source info update
0.0.1:5000
Press CTRL+C to quit
Finished source info update in 0.18 sec
Started build
U index.html
U about/index.html
U projects/index.html
U blog/index.html
U static/style.css
U blog/first-post/index.html
Finished build in 0.82 sec
Started prune
Finished prune in 0.12 sec

````
# Login and Register . 

## What?

- Firebase webapp login and register  for O.A.S.S.P HomePage

- This code uses HTML and JavaScript to create a simple Login/Register web application that utilizes Firebase for authentication. 
- It includes two forms, one for login and another for user registration. 
- It also includes the Firebase JavaScript SDK and initializes the Firebase app using the configuration settings for your Firebase project.
- The login() and register() functions utilize Firebase's authentication methods to sign in or register a user with their email and password. 
- We will modify the firebaseConfig object in the code and add your Firebase project's information.

### Steps

 1. Open gmail and login.

 2. Go to firebase console<https://www.firebase.google.com> and login.

 3. Go to get started and select new Project.
 
````
