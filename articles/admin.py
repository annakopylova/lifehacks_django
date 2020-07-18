from django.contrib import admin

from articles.models import Article, Category, Comments, User
from favourite.models import ArticleFavourite


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('text', 'category_key')
    empty_value_display = 'Пусто'


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user_key')
    empty_value_display = 'Пусто'


@admin.register(ArticleFavourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'user_id')
    empty_value_display = 'Пусто'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'email')
    empty_value_display = 'Пусто'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('approven', 'category_key', 'creation_date')
    empty_value_display = 'Пусто'
    pass
