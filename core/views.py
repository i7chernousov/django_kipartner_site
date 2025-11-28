from django.shortcuts import render
from .models import Category, Article, News


def home(request):
    latest_news = News.objects.filter(is_published=True)[:3]
    return render(request, 'core/home.html', {"latest_news": latest_news})


def services(request):
    categories = Category.objects.filter(section='services')
    return render(request, 'core/services.html', {"categories": categories})


def projects(request):
    categories = Category.objects.filter(section='projects')
    return render(request, 'core/projects.html', {"categories": categories})


def blog(request):
    categories = Category.objects.filter(section='blog')
    return render(request, 'core/blog.html', {"categories": categories})


from .forms import ContactForm

def contacts(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/contacts_success.html')
    else:
        form = ContactForm()

    return render(request, 'core/contacts.html', {"form": form})


def article_detail(request, slug):
    article = Article.objects.filter(slug=slug, is_published=True).first()
    if not article:
        return render(request, 'core/article_not_found.html', status=404)

    return render(request, 'core/article_detail.html', {
        "article": article
    })

def news_list(request):
    news = News.objects.filter(is_published=True)
    return render(request, 'core/news_list.html', {"news": news})

def custom_404(request, exception=None):
    return render(request, 'core/404.html', status=404)

def sitemap_page(request):
    pages = {
        "Главная": "/",
        "Услуги": "/services/",
        "Проекты": "/projects/",
        "Блог": "/blog/",
        "Новости": "/news/",
        "Контакты": "/contacts/",
        "Поиск": "/search/",
    }
    return render(request, 'core/sitemap.html', {"pages": pages})


from django.db.models import Q

def search(request):
    query = request.GET.get("q", "")
    articles = []
    news = []

    if query:
        articles = Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            is_published=True
        )
        news = News.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            is_published=True
        )

    return render(request, 'core/search.html', {
        "query": query,
        "articles": articles,
        "news": news
    })

from django.shortcuts import redirect

def set_theme(request, theme):
    if theme not in ("default", "accessible"):
        theme = "default"

    response = redirect(request.META.get("HTTP_REFERER", "/"))
    response.set_cookie("site_theme", theme, max_age=60*60*24*365)
    return response


from django.contrib.auth import login
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "core/register.html", {"form": form})
