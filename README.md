# Django Template

This is a starter template for Django projects.

## Quickstart

Install the required Python packages:

    pip install -r requirements.txt

Create `.env` file with configuration settings, using `env.sample` as the starting point:

    cp env.sample .env
    nano .env

Run database migrations:

    python manage.py migrate

Run the development server:

    python manage.py runserver


## Automated tests

To run the automated test suite:

    python manage.py test --settings=project.settings.test

