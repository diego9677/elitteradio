from django.views.generic import ListView, TemplateView

from .models import RadioFM


class IndexTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_radios'] = RadioFM.objects.count()
        return context


class RadioFMListView(ListView):
    model = RadioFM
    template_name = 'radio_list.html'

    def get_queryset(self):
        qs = RadioFM.objects.all()
        return qs
