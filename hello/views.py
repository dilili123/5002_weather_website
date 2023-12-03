from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Greeting

# Create your views here.


@csrf_exempt
def index(request):
    return render(request, "index.html")

@csrf_exempt
def about(request):
    return render(request, "team.html")

@csrf_exempt
def contact(request):
    return render(request, "contact.html")


def db(request):
    # If you encounter errors visiting the `/db/` page on the example app, check that:
    #
    # When running the app on Heroku:
    #   1. You have added the Postgres database to your app.
    #   2. You have uncommented the `psycopg` dependency in `requirements.txt`, and the `release`
    #      process entry in `Procfile`, git committed your changes and re-deployed the app.
    #
    # When running the app locally:
    #   1. You have run `./manage.py migrate` to create the `hello_greeting` database table.

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
