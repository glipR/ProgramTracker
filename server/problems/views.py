from django.shortcuts import render
from django.http import HttpResponse

from dashboard.views import webpack_stats_tracker

def problem(request, problem_id=None):
    return HttpResponse(render(request, 'dashboard/vuetify_bundle.html', context={
        'bundle': webpack_stats_tracker.get_tags('problem'),
        'title': 'Index page from Example Django app',
        'problem_id': problem_id,
    }))