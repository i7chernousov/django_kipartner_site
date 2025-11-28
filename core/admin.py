from django.contrib import admin
from .models import Category, Article, News, ContactMessage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "section", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at", "is_published")
    list_filter = ("category", "is_published")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "content")


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "is_published")
    search_fields = ("title", "content")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("name", "email", "subject", "message")
