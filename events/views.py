from django.views.generic import TemplateView


class EventsView(TemplateView):
    template_name = 'events/events.html'


class EventOneView(TemplateView):
    template_name = 'events/event_one.html'


class EventTwoView(TemplateView):
    template_name = 'events/event_two.html'


class EventThreeView(TemplateView):
    template_name = 'events/event_three.html'


class EventFourView(TemplateView):
    template_name = 'events/event_four.html'


class EventFiveView(TemplateView):
    template_name = 'events/event_five.html'
