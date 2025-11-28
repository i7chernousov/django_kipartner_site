from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

handler404 = 'core.views.custom_404'

urlpatterns = [
    path('', views.home, name='home'),

    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('blog/', views.blog, name='blog'),
    path('contacts/', views.contacts, name='contacts'),

    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('news/', views.news_list, name='news'),
    path('sitemap/', views.sitemap_page, name='sitemap'),
    path('search/', views.search, name='search'),
    path('theme/<str:theme>/', views.set_theme, name='set_theme'),

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="core/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
