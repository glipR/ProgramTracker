from django.contrib import admin
from .models import Problem, Submission, Solution, Language

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    pass

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    pass

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass
