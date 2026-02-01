from django import forms
from .models import PurchaseRegistration

class PurchaseRegistrationForm(forms.ModelForm):
    class Meta:
        model = PurchaseRegistration
        fields = ["product_name", "reference_no"]
        widgets = {
            "product_name": forms.TextInput(attrs={"placeholder": "Anong product ang binili?"}),
            "reference_no": forms.TextInput(attrs={"placeholder": "Reference / Receipt number"}),
        }
