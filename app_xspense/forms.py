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
		fields = ('item', 'budget', 'price', 'location')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    def __init__(self, *args, **kwargs):
            super(UserForm, self).__init__(*args, **kwargs)
            self.fields['email'].required = True
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')