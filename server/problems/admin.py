from django.contrib import admin
from .models import Problem, Submission, Solution, Language, WeeklyProblemSelection

@admin.action(description="Update all problem instances")
def update_problem_instances(modeladmin, request, queryset):
    Problem.update_all_problem_instances()

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    actions = [update_problem_instances]

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    pass

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(WeeklyProblemSelection)
class WeekliesAdmin(admin.ModelAdmin):
    pass
