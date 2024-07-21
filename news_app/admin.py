from django.contrib import admin
from .models import News, Categories, Contact

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "published_time", "status", "category"]
    list_filter = ["status", "created_time", "published_time"]
    prepopulated_fields = {"slug": ('title',)}
    date_hierarchy = "published_time"
    search_fields = ["title", "body"]
    ordering = ["status", "published_time"]

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]