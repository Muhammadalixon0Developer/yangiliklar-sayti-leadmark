from menu.models import Category

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "AddPage", 'url_name': 'add_page'},
        {'title': "contact", 'url_name': 'contact'},
        # {'title': "login", 'url_name': 'login'}
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        # cats = Category.objects.annotate(Count('news'))

        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context