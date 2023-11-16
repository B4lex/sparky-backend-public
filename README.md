# Sparky

*Your plans are our duty!*

Sparky is a planning application that automatically schedules daily activities for users.
It allows users to select from pre-defined activities or create custom ones. They can also configure
the randomization frequency, set the time that usually fits for the activity, specify the duration,
and effort it takes. Users can track their progress within the app and make adjustments to their
routine instantly. Furthermore, the app analyzes personal user activity to facilitate their day organization.
It is planned to integrate with various notification systems, such as Google Calendar.

The mission of this app is to automate people's activities and organization routines as much as possible to ease their daily lives.

## This repository contains the Back-end application

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Project structure overview
```
.
└── sparky/
    ├── authorization/
    │   ├── services/ [Logic for OAuth flow management]
    │   └── views.py [Views for Google OAuth flow]
    ├── activities/
    │   ├── api/
    │   │   └── v1/ [URLs, views, and serializer to modify activities]
    │   ├── models/ [Model classes related to the activities and their management]
    │   ├── selectors/ [DB queries related to the activities]
    │   └── services/ [Activities lifecycle management]
    ├── core/ [Project-scoped entities, general utility logic]
    ├── integrations/
    │   ├── adapters/ [Contains adapters implementing single interface interaction with third-party integrations (e.g. Google Calendar)]
    │   ├── models/ [Models encapsulating external integration entities]
    │   └── services/ [Logic layer between models and adapters]
    ├── users/ [User management logic]
    └── utils/ [Contribution project-scoped utilities]
```
Adopted styleguide reference: https://github.com/HackSoftware/Django-Styleguide

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Pre-requisites

In order to have application up and running, first you need to create local envfile in `.envs/.local/`.
The simplest way to accomplish that is to copy `.envs/.test/*` envfiles to `.envs/.local/`.

## Basic Commands

The project uses Docker Compose configuration in order to ease environment deployment everywhere.

### Setting up local project
Build the images from the Docker Compose file:

    $ docker compose -f local.yml build --no-cache

Start containers from the built images:

    $ docker compose -f local.yml up -d

Now, you should have all the project services up and running.

### Executing commands

All the project-related command are needed to be executed out of Docker container.
To do that you need run it along with the following prefix:

    $ docker compose -f local.yml run --rm django <command_to_execute>

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ docker compose run --rm django python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ docker compose -f local.yml run --rm django mypy sparky

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ docker compose -f local.yml run --rm django coverage run -m pytest
    $ docker compose -f local.yml run --rm django coverage html
    $ docker compose -f local.yml run --rm django open htmlcov/index.html

#### Running tests with pytest

    $ docker compose -f local.yml run --rm django pytest

## API Schema

- OpenAPI specification: http://127.0.0.1:8000/api/schema/
- SwaggerUI: http://127.0.0.1:8000/api/docs/

## Celery

This app comes with Celery.

There are three services integrating Celery:
- celeryworker
- celerybeat
- flower

**Flower** lets observe task execution and its performance. By default, it should be accessible under: http://127.0.0.1:5555

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
