from django.shortcuts import render
from django.views.generic import TemplateView


class HomeMatch(TemplateView):
    template_name = "match.html"
