from django import forms
from .models import Budget, Expense, UserProfile
from django.contrib.auth.models import User

class BudgetForm(forms.ModelForm):
	class Meta:
		model = Budget
		fields = ('category', 'purpose', 'amount')

class ExpenseForm(forms.ModelForm):
	class Meta:
		model = Expense
		fields = ('budget', 'item', 'price', 'location')
	def __init__(self, user, *args, **kwargs):
		super(ExpenseForm, self).__init__(**kwargs)
		self.fields['budget'].queryset = Budget.objects.filter(user=user)
		self.fields['budget'].required = True
		self.fields['item'].required = True
		self.fields['price'].required = True

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	def __init__(self, *args, **kwargs):
			super(UserForm, self).__init__(*args, **kwargs)
			self.fields['email'].required = True
			self.fields['username'].help_text = '30 characters maximum'
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'picture')
	def __init__(self, *args, **kwargs):
			super(UserProfileForm, self).__init__(*args, **kwargs)
			self.fields['website'].help_text = 'optional'
			self.fields['picture'].help_text = 'optional'