from django.urls import include, path

from .views import HomeMatch

app_name = "match"
urlpatterns = [
    path("", view=HomeMatch.as_view(), name="match"),
]
