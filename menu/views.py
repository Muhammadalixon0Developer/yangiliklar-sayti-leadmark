from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from .forms import *
from .models import *
from .resources import NewsResources
from .utils import DataMixin, menu


class RegisterUser(DataMixin,CreateView):
    form_class = RegisterUserForm
    template_name = 'page/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='register')
        return {**context, **c_def}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class NewsCategory(DataMixin, ListView):
    model = News
    template_name = 'page/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(cat__slug= self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['menu'] = menu
        # context['title'] = 'Kategorya-' + str(context['posts'][0].cat)
        # context['cat_selected'] = context['posts'][0].cat_id
        c_def = self.get_user_context(title='Bosh sahifa')
        return dict(list(context.items()) + list(c_def.items()))


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    #xabar qo'shuvchi bo'lumning klasi
    form_class = AddPostForm
    template_name = 'page/addpage.html'
    success_url = reverse_lazy('home')
    login_url = '/admin/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['menu'] = menu
        # context['title'] = 'AddPage'
        c_def = self.get_user_context(title='AddPage')
        return {**context, **c_def}


class ShowPost(DataMixin, DetailView):
    # xabarni kengaytirib ko'rsatuvchi funksiyaning o'rniga klass
    model = News
    template_name = 'page/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['menu'] = menu
        # context['title'] = context['post']
        c_def = self.get_user_context(title=context['post'])
        # return dict(list(context.items()) + list(c_def.items()))
        return{**context, **c_def}


class NewsCategory(DataMixin, ListView):
    model = News
    template_name = 'page/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['menu'] = menu
        # context['title'] = 'Kategorya-' + str(context['posts'][0].cat)
        # context['cat_selected'] = context['posts'][0].cat_id
        c_def = self.get_user_context(title='kategoriya-'+str(context['post'][0].cat_id),
                                      cat_selected=context['post'][0].cat_id)
        return context


class NewsHome(ListView):
    # index orniga base class
    paginate_by = 2
    model = News
    template_name = 'page/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['menu'] = menu
        contex['title'] = 'Bosh sahifa'
        contex['cat_selected'] = 0
        return contex

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'page/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='login')
        return {**context, **c_def}

    def get_success_url(self):
        return reverse_lazy('home')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'page/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='contact')
        return {**context, **c_def}

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')

# Funksiyalar


def logout_user(request):
    logout(request)
    return redirect('login')

# def index(request):
#     posts = News.objects.all()
#     cats = Category.objects.all()
#
#     context = {
#         'posts': posts,
#         'cats': cats,
#         'menu': menu,
#         'title': 'Bosh sahifa',
#         'cat_selected': 0,
#     }
#
#     return render(request, 'page/index.html', context=context)

def about(request):
    contact_list = News.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'page/about.html', {'page_obj':page_obj, 'menu': menu, 'title': 'About'})

# def about(request):
#     about = About.objects.all()
#
#     if request.method == 'POST':
#         form = AddAbout(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('about', {'about': about})
#     else:
#         form = AddAbout()
#     return render(request, 'page/about.html', {'form': form, 'title': 'sayt haqida', })


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'page/addpage.html', {'form': form, 'menu': menu, 'title': 'Yangilik qoshish'})


# def contact(request):
#     return HttpResponse("contact")


# def login(request):
#     return HttpResponse("login")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Notogri qadam</h1>')


# def show_post(request, post_slug):
#     #xabarni kengaytirib ko'rsatuvchi funksiya
#     post = get_object_or_404(News, slug=post_slug)
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id
#     }
#
#     return render(request, 'page/post.html', context=context)
#


# def show_category(request, cat_id):
#
#     posts = News.objects.filter(cat_id=cat_id)
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'category',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'page/index.html', context=context)

"""export qilish uchun fiunksiya"""

def export_news(request):
    news_resource = NewsResources()
    data = news_resource.export()
    response = HttpResponse(data.xls, content_type='text/xls')
    response['Content-Disposition'] = 'attachment; filename="news.xls"'
    return response