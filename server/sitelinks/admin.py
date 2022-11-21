from django.contrib import admin
from .models import CodeForcesLink


@admin.register(CodeForcesLink)
class CodeForcesAdminRegister(admin.ModelAdmin):
    pass
