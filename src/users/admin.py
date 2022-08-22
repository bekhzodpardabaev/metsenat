from django.contrib import admin
from .models import CustomUser, Token


class TokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'created_at')


admin.site.register(CustomUser)
admin.site.register(Token, TokenAdmin)
