from django.contrib import admin
from .models import Sport,GameHighlight,User
# Register your models here.

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ['id','name','created_at']

@admin.register(GameHighlight)
class GameHighlightAdmin(admin.ModelAdmin):
    list_display = ['id','title','created_at']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','date_joined']
    ordering = ('-date_joined',)
    search_fields = ['username','id']