from django.views.generic import ListView, TemplateView

from .models import RadioFM


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class RadioFMListView(ListView):
    model = RadioFM
    template_name = 'radio_list.html'

    def get_queryset(self):
        qs = RadioFM.objects.all()
        return qs
