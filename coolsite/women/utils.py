from django.db.models import Count

from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'addpage'},
        {'title': 'Обрантная связть', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
]

class DataMixin:
    paginate_by = 3
    def get_user_context(selfs, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('women'))

        user_menu = menu.copy()
        if not selfs.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected']=0
        return context