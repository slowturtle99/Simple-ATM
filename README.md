# Simple-ATM

## Prerequisites

+ python 3.10.x
+ django 4.0.6

To create python virtual environment using conda
~~~shell
$ conda create -n atm_env python=3.10
~~~
To install django
~~~shell
$ conda activate atm_env
$ conda install -c conda-forge django==4.0.6
~~~

## Installation
Clone this repository
~~~shell
$ git clone https://github.com/slowturtle99/Simple-ATM.git
~~~


## Test

~~~shell
$ cd ~/Simple-ATM
~~~
Run
~~~shell
$ python manage.py runserver
~~~
Output
~~~shell
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 13, 2022 - 13:44:33
Django version 4.0.6, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
~~~
### To test atm
Open this link using a browser.  
http://127.0.0.1:8000/atm/

Two cards are saved in DB for testing.   
Card number: 111122223333 | PIN: 3333  
Card number: 444455556666 | PIN: 6666


### To manage cards and accounts
http://127.0.0.1:8000/admin/

Username: admin | Password: 1111