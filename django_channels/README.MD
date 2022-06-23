# Django Channels

Channels is a project that takes Django and extends its abilities beyond HTTP - to handle WebSockets, chat protocols, IoT protocols, and more. It’s built on a Python specification called ASGI.

Channels builds upon the native ASGI support available in Django since v3.0, and provides an implementation itself for Django v2.2. Django still handles traditional HTTP, whilst Channels give you the choice to handle other connections in either a synchronous or asynchronous style.



## Installation

Install all the dependancy using following command's

```
virtualenv venv   #create virtual environment
source /venv/bin/activate      # Activate vertual environment

pip install -r requirement.txt

```

## Usage

Use Websocketking website to connect with websocket

```
https://websocketking.com/

ws://localhost:8000/ws/new/
ws://localhost:8000/ws/test/
```

makemigations & migrate & runserver

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```

goto your browser open to diffrent tab

```
#for see rendered data in the web page

http://127.0.0.1:8000/              

#for creating the data into the backend 

http://127.0.0.1:8000/students/?total=100 

```

