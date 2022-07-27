from django.urls import path
from . import views
from .views import NewsList, NewsDetail, UserCreate, LoginUser

urlpatterns = [
    path('', NewsList.as_view(), name='home_page'),
    path('news_detail/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('category/<int:pk>/', views.category, name='category'),
    path('register/', UserCreate.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('parse/', views.parse, name='parse'),
    path('search/', views.search, name='search'),
]
