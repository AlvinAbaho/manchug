# from membership.forms import ContactForm
from manchug.forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView


class HomePageView(FormView):
    template_name = 'home.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        print("good form\n")
        form.send_email()
        return super().form_valid(form)


# class HomePageView(TemplateView):
#     template_name = 'home.html'
