from django.forms import ModelForm
from main.models import ThriftEntry
from django.utils.html import strip_tags


class ThriftEntryForm(ModelForm):
    class Meta:
        model = ThriftEntry
        fields = ["name", "price", "description", "condition"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

    def clean_condition(self):
        condition = self.cleaned_data["condition"]
        return strip_tags(condition)