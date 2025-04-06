from django.views.generic import ListView

from .models import RadioFM


class RadioFMListView(ListView):
    model = RadioFM
    template_name = 'index.html'

    def get_queryset(self):
        qs = RadioFM.objects.all()
        return qs
