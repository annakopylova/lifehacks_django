from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from articles import articlesapi


def get_article(article_id):
    return articlesapi.get_article(article_id)


@csrf_exempt
def add_article(request):
    text = request.POST['title']
    description = request.POST['description']
    category_key = request.POST['sectionGUID']
    user_key = request.POST['userGUID']
    token = request.POST['token']
    newdoc = request.FILES['docfile']
    return JsonResponse(articlesapi.add_article(text, description, category_key, user_key, token, newdoc))


@csrf_exempt
def get_map(request):
    category_key = request.POST['sectionGUID']
    user_key = request.POST['userGUID']
    token = request.POST['token']
    return JsonResponse(articlesapi.get_map(category_key, user_key, token))


@csrf_exempt
def get_sections(request):
    user_key = request.GET['userGUID']
    token = request.GET['token']
    return JsonResponse(articlesapi.get_sections(user_key, token))


@csrf_exempt
def get_all_articles(request):
    category_key = request.GET['sectionGUID']
    user_key = request.GET['userGUID']
    token = request.GET['token']
    return JsonResponse(articlesapi.get_all_articles(category_key, user_key, token))


@csrf_exempt
def get_all_comments(request):
    article_key = request.GET['articleGUID']
    user_key = request.GET['userGUID']
    token = request.GET['token']
    return JsonResponse(articlesapi.get_all_comments(article_key, user_key, token))


@csrf_exempt
def add_comment(request):
    article_key = request.GET['articleGUID']
    user_key = request.GET['userGUID']
    token = request.GET['token']
    message = request.GET['message']
    return JsonResponse(articlesapi.add_comment(article_key, message, user_key, token))


@csrf_exempt
def detail(request, article_id):
    user_key = request.POST['userGUID']
    token = request.POST['token']
    # user_key = '123'
    # token = '123'
    return JsonResponse(articlesapi.get_article(article_id, user_key, token))


def index(request):
    return None
