from django.http import JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views, favouriteapi


@csrf_exempt
def favourite(request):
    article_id = request.GET['articleGUID']
    user_key = request.GET['userGUID']
    token = request.GET['token']
    status = request.GET['status']
    return JsonResponse(favouriteapi.set_favourite(article_id, user_key, token, status))


@csrf_exempt
def like(request):
    article_id = request.GET['articleGUID']
    user_key = request.GET['userGUID']
    token = request.GET['token']
    status = request.GET['status']
    return JsonResponse(favouriteapi.set_like(article_id, user_key, token, status))
