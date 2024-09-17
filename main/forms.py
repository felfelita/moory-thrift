from django.forms import ModelForm
from main.models import ThriftEntry

class ThriftEntryForm(ModelForm):
    class Meta:
        model = ThriftEntry
        fields = ["name", "price", "description", "condition"]