# Phonebook Webapp

It is a simple yet modern phonebook to create contact and add multiple numbers for each contact. Developed using Django Framework. 


## Database Schema
![DB_Diagram](https://user-images.githubusercontent.com/94204070/232232280-20d2625c-95a3-474d-bf1e-f058fb9f733b.png)
## Repository Tree
```
Simple Phonebook
├─ db.sqlite3
├─ docker-compose.yml
├─ Dockerfile
├─ main
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  ├─ __init__.py
├─ manage.py
├─ phonebook
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  ├─ __init__.py
├─ requirements.txt
└─ templates
   ├─ contact_detail.html
   ├─ header.html
   ├─ includes
   │  └─ navbar.html
   ├─ new_contact.html
   └─ show_contacts.html
```
## Prerequisites

I assume you have installed Docker and Docker Compose (or Docker Engine if you are on windows) and it is running.

See the [Docker website](http://www.docker.io/gettingstarted/#h_installation) for installation instructions.


## Installation

1. Clone this repo

```
git clone https://github.com/KarimOussama1/Simple-Phonebook.git
```

2. Navigate to the cloned repo

3. Simply you need to build and run the `docker-compose.yml` file using the following commands:

```bash
  docker-compose build
  docker-compose up
```

4. Once it is finished, Navigate to http://localhost:8000 in your web browser to use the Phonebook app.
