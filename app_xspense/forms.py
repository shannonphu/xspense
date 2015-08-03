from django import forms
from .models import Budget
from .models import Expense

class BudgetForm(forms.ModelForm):
	class Meta:
		model = Budget
		fields = ('category', 'purpose', 'amount')

class ExpenseForm(forms.ModelForm):
	class Meta:
		model = Expense
		fields = ('item', 'budget', 'price', 'location')