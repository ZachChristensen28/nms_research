# SURVEY VIEWS.PY
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model


User = get_user_model()


class StartSurveyView(LoginRequiredMixin, TemplateView):
    template_name = 'survey/start.html'


class StartTaskView(LoginRequiredMixin, TemplateView):
    template_name = 'survey/task.html'
