from django.forms import model_to_dict

from django.http import HttpResponse, JsonResponse
from favourite import favouriteapi
from user.views import find_user_by_token, find_user
from utils.Utils import generate_random_key
from .models import *
from datetime import date, datetime


# user: postgres
# password: admin

def get_article(article_id, user_key, token):
    user = find_user_by_token(user_key, token)
    if user is not None and user.token_expiration > datetime.now().date():
        # получаем статью с таким ключом
        # возвращаем эту статью
        articles = Article.objects.filter(article_key=article_id)
        if len(articles) == 0:
            return {
                "success": False
            }
        else:
            response = {'success': True, 'data': model_to_dict(articles[0])}
            response['data']['docfile'] = str(articles[0].docfile)
            del response['data']['id']
            del response['data']['approven']
            response['data']['favourite'] = favouriteapi.get_favourite(article_id, user_key)
            return response
    else:
        return {
            "success": False
        }


def add_article(title, description, category_key, user_key, token, newdoc):
    user = find_user_by_token(user_key, token)
    if user is not None and user.token_expiration > datetime.now().date():
        # Создаем рандомный ключ
        key = generate_random_key(63)
        # создаем статью, кладем ее в бд
        article = Article.objects.create(article_key=key,
                                         title=title, description=description,
                                         docfile=newdoc,
                                         category_key=category_key,
                                         creation_date=datetime.now())
        article.save()
        # возвращаем статью
        response = {'data': model_to_dict(article), 'success': True}
        response['data']['docfile'] = str(article.docfile)

        response['data']['like_count'] = 0
        response['data']['favourite'] = False
        response['data']['author'] = user.login
        response['data']['liked'] = False

        d = response['data']['creation_date']
        dt = d.timestamp()
        del response['data']['creation_date']
        response['data']['creation_date'] = dt

        del response['data']['id']
        del response['data']['approven']
        return response
    else:
        return {
            "success": False
        }


def get_map(category_key, user_key, token):
    user = find_user_by_token(user_key, token)
    if user is not None and user.token_expiration > datetime.now().date():
        articles = Article.objects.filter(category_key=category_key)

        dict = list(articles.values())

        response = {'success': True, 'data': dict}

        for i in dict:
            file = str(i['docfile'])
            del i['docfile']
            del i['id']
            del i['approven']
            i['docfile'] = file

        return response
    else:
        return {
            "success": False
        }


def get_sections(user_key, token):
    user = find_user_by_token(user_key, token)
    if user is not None and user.token_expiration > datetime.now().date():
        categories = Category.objects.all()

        dict = list(categories.values())

        response = {'success': True, 'data': dict}

        return response
    else:
        return {
            "success": False
        }


def add_comment(article_key, message, user_key, token):
    user = find_user_by_token(user_key, token)
    if user is not None and user.token_expiration > datetime.now().date():

        comment = Comments.objects.create(comment_key=generate_random_key(63),
                                          user_key=user_key,
                                          article_key=article_key,
                                          text=message,
                                          creation_date=datetime.now())

        comments = Comments.objects.filter(article_key=article_key)
        dict = list(comments.values())

        response = {'success': True, 'data': dict}

        for i in dict:
            del i['id']
            i['name'] = find_user(i['user_key']).login
            d = i['creation_date']
            dt = d.timestamp()
            del i['creation_date']
            i['creation_date'] = dt

        return response
    else:
        return {
            "success": False
        }


def get_all_comments(article_key, user_key, token):
    user = find_user_by_token(user_key, token)
    if user is not None and user.token_expiration > datetime.now().date():
        comments = Comments.objects.filter(article_key=article_key)
        dict = list(comments.values())

        response = {'success': True, 'data': dict}

        for i in dict:
            del i['id']
            i['name'] = find_user(i['user_key']).login
            d = i['creation_date']
            dt = d.timestamp()
            del i['creation_date']
            i['creation_date'] = dt

        return response
    else:
        return {
            "success": False
        }


def get_all_articles(category_key, user_key, token):
    user = find_user_by_token(user_key, token)
    if user is not None and user.token_expiration > datetime.now().date():
        articles = Article.objects.filter(category_key=category_key, approven=1)

        dict = list(articles.values())

        for i in dict:
            docfile = i['docfile']
            if docfile is None:
                docfile = i['image_path']
                file = docfile
            else:
                file = "$%" + str(i['docfile'])

            del i['image_path']
            d = i['creation_date']
            dt = d.timestamp()
            del i['creation_date']
            del i['docfile']
            del i['id']
            del i['approven']
            i['creation_date'] = dt
            i['docfile'] = file
            i['favourite'] = favouriteapi.get_favourite(i['article_key'], user_key)
            i['like_count'] = favouriteapi.get_like_count(i['article_key'])
            i['liked'] = favouriteapi.get_like(i['article_key'], user_key)
            i['author'] = find_user(user_key).login

        print(dict)

        response = {'success': True, 'data': dict}

        return response
    else:
        return {
            "success": False
        }
