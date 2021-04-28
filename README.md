
# Rest API
## Quick start

```bash
$ # Get the code
$ git clone https://github.com/creativetimofficial/black-dashboard-django.git
$ cd black-dashboard-django
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the app 
$ # python manage.py runserver
$
$ # Access the web app in browser: http://127.0.0.1:8000/
