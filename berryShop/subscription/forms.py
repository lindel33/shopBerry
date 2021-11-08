from django import forms
from .models import Subscription


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = ("email", )
        widgets = {
            "email": forms.TextInput(attrs={"class": "editContent"})

        }