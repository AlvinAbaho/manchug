from django.views.generic import TemplateView


class EventsView(TemplateView):
    template_name = 'events/events.html'


class EventDetailView(TemplateView):
    template_name = 'events/event_detail_view.html'
