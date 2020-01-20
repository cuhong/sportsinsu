from crispy_forms.helper import FormHelper
from django import forms

from event.models import Event


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'main_image', 'event_start', 'event_end', 'insu_rgst_start', 'insu_rgst_end',
                  'description']

    def __init__(self, *args, **kwargs):
        super(EventCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.form_method = 'POST'