from django.shortcuts import render
from django.urls import reverse_lazy

from .models import News, Category, Author
from .forms import RegisterUserForm, LoginUserForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .parse import parsing
from django.core.paginator import Paginator

# Create your views here.


#def home_page(request):
#    news = News.objects.all()
#    return render(request, "main/base.html", {'news': news})


class NewsList(ListView):
    model = News
    paginate_by = 10
    template_name = "main/home_page.html"
    context_object_name = 'news'


#def news_detail(request, pk):
#    news = News.objects.get(pk=pk)
#   return render(request, "main/news_detail.html", {'news': news})

class NewsDetail(DetailView):
    model = News
    template_name = "main/news_detail.html"
    context_object_name = 'news'


def category(request, pk):
    news_by_category = News.objects.filter(category_id=pk)
    category_name = Category.objects.get(pk=pk)
    paginator = Paginator(news_by_category, 10)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, "main/news_by_category.html", {'news_by_category': news_by_category, 'category_name': category_name, 'page_obj': page_obj, })


class UserCreate(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('home_page')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "main/login.html"

    def get_success_url(self):
        return reverse_lazy('home_page')


def user_logout(request):
    logout(request)
    return redirect('home_page')


def parse(request):
    news_list = parsing()
    i = 0
    while i < len(news_list):
        news = News(header=news_list[i]['header'], annotation=news_list[i]['annotation'], text=news_list[i]['full_text'], category=Category.objects.get(category_name='Хабр'), author=Author.objects.get(name='Хабр'), photo_url=news_list[i]['image'])
        news.save()
        i = i + 1
    return redirect('home_page')


def search(request):
    news_by_category = ''
    if request.GET.get('search'):
        search_form = request.GET.get('search')
        news_by_category = News.objects.filter(header__icontains=search_form)
        paginator = Paginator(news_by_category, 10)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
    return render(request, "main/search.html", {'news_by_category': news_by_category, })







