from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class LogoutView(TemplateView):
    template_name = 'logout.html'
