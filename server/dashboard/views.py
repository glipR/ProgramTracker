import json
import pathlib

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings


class WebpackStatsProcessing:
    def __init__(self):
        self.data = json.loads(pathlib.Path(settings.STATS_FILE).read_text("utf-8"))

    def get_tags(self, bundle: str) -> str:
        include_tags = []
        for asset in self.data["chunks"][bundle]:
            if asset.endswith(".map"):
                continue

            location = self.data["assets"][asset]["publicPath"]
            if asset.endswith((".js", "js.gz")):
                include_tags.append(
                    f'<link href="{location}" rel="preload" as="script" />'
                )
                include_tags.append(
                    f'<script type="text/javascript" src="{location}"></script>'
                )
            if asset.endswith((".css", ".css.gz")):
                include_tags.append(
                    f'<link href="{location}" rel="stylesheet preload" as="style" />'
                )
        return "\n".join(include_tags)


webpack_stats_tracker = WebpackStatsProcessing()

from server.views import login_view, logout_view, register_view


def index(request):
    if request.method == "POST":
        if request.POST["post_type"] == "login":
            return login_view(request)
        elif request.POST["post_type"] == "logout":
            return logout_view(request)
        elif request.POST["post_type"] == "register":
            return register_view(request)
    return HttpResponse(
        render(
            request,
            "dashboard/vuetify_bundle.html",
            context={
                "bundle": webpack_stats_tracker.get_tags("index"),
                "title": "Index page from Example Django app",
                "user_id": request.user.id,
            },
        )
    )
