from datetime import datetime

from favourite.models import ArticleFavourite
from user.views import find_user_by_token


def set_favourite(article_id, user_key, token, status):
    user = find_user_by_token(user_key, token)
    if user is not None and user.token_expiration > datetime.now().date():
        # получаем статью с таким ключом
        # возвращаем эту статью
        boolstatus = status == 'true'
        articles = ArticleFavourite.objects.filter(article_id=article_id, user_id=user_key)
        if len(articles) == 0:
            article = ArticleFavourite(article_id=article_id, user_id=user_key, favourite=boolstatus, like=False)
            article.save()
            return {'success': True, 'data': {'article_id': article_id, 'favourite': boolstatus}}
        else:
            articlefav = articles[0]
            articlefav.favourite = boolstatus
            articlefav.save()
            return {'success': True, 'data': {'article_id': article_id, 'favourite': boolstatus}}
    else:
        return {
            "success": False
        }


def set_like(article_id, user_key, token, status):
    user = find_user_by_token(user_key, token)
    if user is not None and user.token_expiration > datetime.now().date():
        # получаем статью с таким ключом
        # возвращаем эту статью
        boolstatus = status == 'true'
        articles = ArticleFavourite.objects.filter(article_id=article_id, user_id=user_key)
        if len(articles) == 0:
            article = ArticleFavourite(article_id=article_id, user_id=user_key, like=boolstatus, favourite=False)
            article.save()
            return {'success': True, 'data': {'article_id': article_id, 'liked': boolstatus}}
        else:
            articlefav = articles[0]
            articlefav.like = boolstatus
            articlefav.save()
            return {'success': True, 'data': {'article_id': article_id, 'liked': boolstatus}}
    else:
        return {
            "success": False
        }


def get_favourite(article_id, user_id):
    articles = ArticleFavourite.objects.filter(article_id=article_id, user_id=user_id)
    if len(articles) == 0:
        return False
    else:
        return articles[0].favourite


def get_like(article_id, user_id):
    articles = ArticleFavourite.objects.filter(article_id=article_id, user_id=user_id)
    if len(articles) == 0:
        return False
    else:
        return articles[0].like


def get_count_of_favourites(article_id):
    articles = ArticleFavourite.objects.filter(article_id=article_id, favourite=True)
    return len(articles)


def get_like_count(article_id):
    articles = ArticleFavourite.objects.filter(article_id=article_id, like=True)
    return len(articles)