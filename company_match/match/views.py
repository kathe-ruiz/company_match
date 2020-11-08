from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import userBioForm
from .torreIntegration import TorreIntegration

class HomeMatch(FormView):
    template_name = "match.html"
    form_class = userBioForm
    success_url = reverse_lazy("match:match")

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        return self.render_to_response(self.get_context_data())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get("username")
        if username is not None:
            torreIntegration = TorreIntegration()
            bio = torreIntegration.get_bio(username)
            context["bio"] = bio.json()["person"]
        return context