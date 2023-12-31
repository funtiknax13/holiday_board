from django.contrib import admin

from board.models import Message


# Register your models here.
@admin.register(Message)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'is_public')
    list_filter = ('is_public', )

    actions = ['clear_debt']

    @admin.action(description='Опубликовать')
    def clear_debt(self, request, queryset):
        queryset.update(is_public=True)
