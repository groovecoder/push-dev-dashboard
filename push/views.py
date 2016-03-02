from django.views.generic import TemplateView

from push.forms import VapidValidationForm
from push.models import generate_jws_key_token

class PushApplication(TemplateView):
    template_name = 'push/details.html'

    def get_context_data(self, **kwargs):
        context = super(PushApplication, self).get_context_data(**kwargs)
        context['vapid_validation_form'] = VapidValidationForm()
        context['jws_token'] = generate_jws_key_token()
        return context
