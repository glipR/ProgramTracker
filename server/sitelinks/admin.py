from django.contrib import admin
from .models import CodeForcesLink

@admin.action(description="Update the latest submissions of all selected users")
def update_submissions(modeladmin, request, queryset):
    for obj in queryset:
        print(obj.get_new_submissions())

@admin.register(CodeForcesLink)
class CodeForcesAdminRegister(admin.ModelAdmin):
    actions = [update_submissions]
