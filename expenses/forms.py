from .models import Budget, Expense
from django import forms

class ExpenseForm(forms.ModelForm):
    class Meta:

        model = Expense
        
        fields = ("amount", "content", "category", "source", "date", "owner")
        exclude = ["owner"]

        widgets = {
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
            "content": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "source": forms.TextInput(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={"class": "form-control"}),
        }


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        
        fields = ("amount", "owner")
        exclude = ["owner"]

        widgets = {"amount": forms.NumberInput(attrs={"class": "form-control"})}

# forms.py
from django import forms

class BudgetFormPrediction(forms.Form):
    monthly_budget = forms.FloatField(label="Enter Monthly Budget", min_value=0)
    saving_goal = forms.FloatField(label="Enter Saving Goal", min_value=0)

