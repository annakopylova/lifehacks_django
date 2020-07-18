import random
import string
from datetime import datetime as datetimes
import datetime

from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from articles.models import User


def signup(request):
    login = request.GET['login']
    email = request.GET['email']
    password = request.GET['password']
    if User.objects.all().filter(email=email).__len__() == 0:
        user = User(login=login,
                    email=email,
                    password=password)
        user.user_key = generate_token()
        prolong_token(user)
        user.save()

        user = User.objects.all().filter(email=email, login=login, password=password).first()
        json_returns = {
            "success": True,
            "user_key": user.user_key,
            "email": user.email,
            "token": user.token
        }
    else:
        json_returns = {
            "success": False
        }

    return JsonResponse(json_returns, safe=False)


def signin(request):
    login = request.GET['input']
    password = request.GET['password']

    users = User.objects.all().filter(login=login, password=password)
    if len(users) == 0:
        json_returns = {
            "success": False
        }
    else:
        user = users.first()
        user.token = generate_token()
        prolong_token(user)
        user.save()
        json_returns = {
            "success": True,
            "user_key": user.user_key,
            "email": user.email,
            "token": user.token
        }
    return JsonResponse(json_returns, safe=False)


def find_user_by_token(user_key, token):
    users = User.objects.all().filter(user_key=user_key, token=token)
    if len(users) == 0:
        return None
    else:
        return users.first()


def find_user(user_key):
    users = User.objects.all().filter(user_key=user_key)
    if len(users) == 0:
        return None
    else:
        return users.first()


def prolong_token(user):
    user.token = generate_token()
    user.token_expiration = datetimes.now() + datetime.timedelta(days=21)
    user.save()


def generate_token():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(511))