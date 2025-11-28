from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    SECTION_CHOICES = [
        ('services', 'Услуги'),
        ('projects', 'Проекты'),
        ('blog', 'Блог'),
    ]

    name = models.CharField("Название категории", max_length=100)
    slug = models.SlugField("URL-адрес", unique=True)
    section = models.CharField(
        "Раздел",
        max_length=20,
        choices=SECTION_CHOICES
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.get_section_display()}: {self.name}"


class Article(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="articles",
        verbose_name="Категория"
    )
    title = models.CharField("Название", max_length=200)
    slug = models.SlugField("URL-адрес", unique=True)
    content = models.TextField("Содержание")
    image = models.ImageField(
        "Изображение",
        upload_to="articles/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)
    is_published = models.BooleanField("Опубликовано", default=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Текст новости")
    created_at = models.DateTimeField("Дата", auto_now_add=True)
    is_published = models.BooleanField("Опубликовано", default=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новое'),
        ('in_progress', 'В обработке'),
        ('done', 'Обработано'),
    ]

    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("E-mail")
    subject = models.CharField("Тема", max_length=200)
    message = models.TextField("Сообщение")
    created_at = models.DateTimeField("Отправлено", auto_now_add=True)
    status = models.CharField(
        "Статус",
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )
    manager = models.ForeignKey(
        User,
        verbose_name="Менеджер",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Сообщение с сайта"
        verbose_name_plural = "Сообщения с сайта"

    def __str__(self):
        return f"{self.subject} ({self.email})"
