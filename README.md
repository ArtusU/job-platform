### Getting Started

1. Pull the repository
2. Build the docker image with `docker-compose -f local.yml build`
3. Continue with the installation procedure outlined in the [Cookiecutter Django docs](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html)
4. `docker-compose -f local.yml run --rm django python manage.py migrate`
5. `docker-compose -f local.yml run --rm django python manage.py createsuperuser`
6. `docker-compose -f local.yml up`

This project is built using [Cookiecutter Django](http://cookiecutter-django.readthedocs.io).