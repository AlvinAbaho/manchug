from django.views.generic import TemplateView


class CommitteeView(TemplateView):
    template_name = 'committee/committee.html'
